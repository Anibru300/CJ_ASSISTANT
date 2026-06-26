#!/usr/bin/env python3
"""
Análisis de reconciliación entre vales y facturas.

Lee BD_ALMACEN_3P.xlsx (hojas VALES y DETALLE_VALES) y detecta:
1. Vales con facturación parcial (comentarios con múltiples facturas).
2. Líneas de vale con múltiples facturas en NO_FACTURA.
3. Líneas donde cantidad original != cantidad viva + ajustada.
4. Vales abiertos con todos los códigos en cantidad viva = 0 (posible error de estado).
5. Vales cerrados con alguna línea con cantidad viva > 0 (posible error de estado).

No requiere conexión a SAE. Usa solo el Excel de almacén.
"""

import re
from pathlib import Path

import pandas as pd


def normalize_text(value):
    if pd.isna(value):
        return ""
    return str(value).strip().upper()


def extract_invoices(no_factura):
    """Extrae lista de facturas de un campo que puede tener varias separadas por coma, /, etc."""
    text = normalize_text(no_factura)
    if not text or text in ("NAN", "0", "0.0", "N/A", "NA"):
        return []
    # Separar por comas, punto y coma, slash, y
    parts = re.split(r"[,;/]|\s+Y\s+", text, flags=re.IGNORECASE)
    invoices = []
    for p in parts:
        p = p.strip()
        # Buscar patrones tipo A1234, A-1234, 12345
        if re.match(r"^[A-Z]?[-]?\d+$", p, re.IGNORECASE):
            invoices.append(p.upper())
    return invoices


def has_partial_invoice_comment(comment):
    """Detecta comentarios que indican facturación parcial."""
    text = normalize_text(comment)
    keywords = [
        "FACTURANDO",
        "PENDIENTE POR FACTURAR",
        "FALTAN DE FACTURAR",
        "SE FACTURARA",
        "FALTA FACTURA",
        "FACT:",
        "FAC ",
        "MANUAL:",
        "AJUSTE MANUAL",
    ]
    return any(k in text for k in keywords)


def main():
    base_dir = Path(__file__).resolve().parents[3]
    input_file = base_dir / "workspace" / "almacen" / "data" / "BD_ALMACEN_3P_20260625.xlsx"
    output_dir = base_dir / "workspace" / "almacen" / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"[INFO] Leyendo {input_file.name}...")
    vales = pd.read_excel(input_file, sheet_name="VALES")
    detalle = pd.read_excel(input_file, sheet_name="DETALLE_VALES")

    # Normalizar columnas numéricas
    for col in ["FOLIO_VALE", "CANTIDAD", "CANTIDAD_VIVA", "CANT_AJUSTADA", "CANT_ASIGNADA_PEDIDO"]:
        detalle[col] = pd.to_numeric(detalle[col], errors="coerce")

    # Limpiar columnas de texto
    detalle["STATUS"] = detalle["STATUS"].astype(str).str.strip().str.upper()
    detalle["NO_FACTURA_STR"] = detalle["NO_FACTURA"].fillna("").astype(str).str.strip()
    detalle["COMENTARIO"] = detalle["COMENTARIOS_ADICIONALES"].fillna("").astype(str).str.strip()

    findings = []

    # 1. Líneas con múltiples facturas en NO_FACTURA
    detalle["FACTURAS_LISTA"] = detalle["NO_FACTURA_STR"].apply(extract_invoices)
    detalle["NUM_FACTURAS"] = detalle["FACTURAS_LISTA"].apply(len)
    multi_fact = detalle[detalle["NUM_FACTURAS"] > 1].copy()
    for _, row in multi_fact.iterrows():
        findings.append({
            "tipo": "Múltiples facturas en NO_FACTURA",
            "folio_vale": row["FOLIO_VALE"],
            "codigo": row["CODIGO"],
            "cantidad": row["CANTIDAD"],
            "cantidad_viva": row["CANTIDAD_VIVA"],
            "facturas": ", ".join(row["FACTURAS_LISTA"]),
            "comentario": row["COMENTARIO"],
            "accion_sugerida": "Verificar cantidad facturada por cada factura en SAE",
        })

    # 2. Líneas con comentarios de facturación parcial
    partial = detalle[detalle["COMENTARIO"].apply(has_partial_invoice_comment)].copy()
    for _, row in partial.iterrows():
        if row["NUM_FACTURAS"] <= 1:  # evitar duplicar con el anterior
            findings.append({
                "tipo": "Facturación parcial detectada en comentario",
                "folio_vale": row["FOLIO_VALE"],
                "codigo": row["CODIGO"],
                "cantidad": row["CANTIDAD"],
                "cantidad_viva": row["CANTIDAD_VIVA"],
                "facturas": row["NO_FACTURA_STR"],
                "comentario": row["COMENTARIO"],
                "accion_sugerida": "Cruzar con facturas de SAE para calcular cantidad viva real",
            })

    # 3. Líneas donde cantidad original != cantidad viva + ajustada y NO hay factura ni comentario de facturacion
    detalle["SUMA_AJUSTES"] = detalle["CANTIDAD_VIVA"].fillna(0) + detalle["CANT_AJUSTADA"].fillna(0)
    detalle["DIFERENCIA"] = detalle["CANTIDAD"].fillna(0) - detalle["SUMA_AJUSTES"]
    diff = detalle[abs(detalle["DIFERENCIA"]) > 0.001].copy()
    for _, row in diff.iterrows():
        # Si tiene factura o comentario de facturacion, la diferencia se explica; omitir
        if row["NUM_FACTURAS"] >= 1 or has_partial_invoice_comment(row["COMENTARIO"]):
            continue
        findings.append({
            "tipo": "Cantidad original no coincide con viva + ajustada (sin factura registrada)",
            "folio_vale": row["FOLIO_VALE"],
            "codigo": row["CODIGO"],
            "cantidad": row["CANTIDAD"],
            "cantidad_viva": row["CANTIDAD_VIVA"],
            "facturas": row["NO_FACTURA_STR"],
            "comentario": row["COMENTARIO"],
            "accion_sugerida": "Revisar si el material se facturo en SAE pero no se registro en el Excel",
        })

    # 4. Vales abiertos con todas las líneas en cantidad viva = 0
    grouped = detalle.groupby("FOLIO_VALE").agg({
        "CANTIDAD_VIVA": "sum",
        "STATUS": "first",
    }).reset_index()
    open_zero = grouped[(grouped["STATUS"] == "ABIERTO") & (grouped["CANTIDAD_VIVA"] == 0)]
    for _, row in open_zero.iterrows():
        findings.append({
            "tipo": "Vale abierto pero cantidad viva total = 0",
            "folio_vale": row["FOLIO_VALE"],
            "codigo": "(varios)",
            "cantidad": None,
            "cantidad_viva": 0,
            "facturas": "",
            "comentario": "",
            "accion_sugerida": "Verificar si el vale debería estar CERRADO",
        })

    # 5. Vales cerrados con alguna línea con cantidad viva > 0
    closed_alive = detalle[(detalle["STATUS"] == "CERRADO") & (detalle["CANTIDAD_VIVA"] > 0)]
    for _, row in closed_alive.iterrows():
        findings.append({
            "tipo": "Vale cerrado pero con cantidad viva > 0",
            "folio_vale": row["FOLIO_VALE"],
            "codigo": row["CODIGO"],
            "cantidad": row["CANTIDAD"],
            "cantidad_viva": row["CANTIDAD_VIVA"],
            "facturas": row["NO_FACTURA_STR"],
            "comentario": row["COMENTARIO"],
            "accion_sugerida": "Verificar por qué el vale está cerrado si aún hay cantidad viva",
        })

    df_findings = pd.DataFrame(findings)

    # Resumen
    summary = df_findings["tipo"].value_counts().reset_index()
    summary.columns = ["tipo", "cantidad"]

    output_file = output_dir / "vale_factura_hallazgos.xlsx"
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        df_findings.to_excel(writer, sheet_name="Hallazgos", index=False)
        summary.to_excel(writer, sheet_name="Resumen", index=False)

    print(f"[OK] Reporte generado: {output_file}")
    print("\nResumen:")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
