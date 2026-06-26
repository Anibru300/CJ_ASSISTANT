# Knowledge Coverage Matrix — CJ_OS

**Versión:** 0.3.0  
**Fecha:** 2026-06-25  
**Estado:** Plantilla maestra — pendiente de uso en KES  
**Propósito:** Medir cuánto conocimiento se ha adquirido de cada dominio. Una KES no termina por conversación; termina por cobertura.

---

## 1. ¿Qué mide esta matriz?

La matriz mide, por dominio y por categoría de conocimiento, el porcentaje capturado y validado.

> **Una KES termina cuando la cobertura de las categorías críticas supera el umbral definido (típicamente 90%).**

---

## 2. Leyenda

| Símbolo | Significado |
|---------|-------------|
| ✅ | Completo / ≥ 90% |
| 🟢 | Avanzado / 70-89% |
| 🟡 | En progreso / 40-69% |
| 🔴 | Bajo / 20-39% |
| ⚪ | Sin iniciar / < 20% |

---

## 3. Matriz global

| Dominio | Términos | Actores | Objetos | Eventos | Procesos | Reglas | Excepciones | Decisiones | KPIs | Automatizaciones | Estado general |
|---------|----------|---------|---------|---------|----------|--------|-------------|------------|------|------------------|----------------|
| **D0 Lenguaje Empresarial** | 🟡 | — | — | — | — | — | — | — | — | — | 🟡 En preparación |
| **D1 Dirección** | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ Pendiente |
| **D2 Ventas** | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ Pendiente |
| **D3 Compras** | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ Pendiente |
| **D4 Almacén** | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟡 | 🟢 | 🟢 | ⚪ | 🟢 Avanzado |
| **D5 Logística** | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ Pendiente |
| **D6 Calidad** | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ Pendiente |
| **D7 Contabilidad** | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ Pendiente |
| **D8 RRHH** | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ Pendiente |
| **D9 Inteligencia Empresarial** | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ Pendiente |

---

## 4. Detalle por dominio

### D0 — Lenguaje Empresarial (KES-0, en preparación)

| Categoría | Ítems esperados | Ítems capturados | Validados | Cobertura | Estado |
|-----------|-----------------|------------------|-----------|-----------|--------|
| Términos transversales | 15 | 10 | 0 | 0% | 🟡 |

> **Nota:** Los términos iniciales están documentados. La KES-0 validará significados, sinónimos y propietarios.

### D4 — Almacén (en preparación)

| Categoría | Ítems esperados | Ítems capturados | Validados | Cobertura | Estado |
|-----------|-----------------|------------------|-----------|-----------|--------|
| Actores | 7 | 7 | 6 | 86% | 🟢 |
| Objetos | 11 | 10 | 9 | 82% | 🟢 |
| Eventos | 14 | 12 | 11 | 79% | 🟢 |
| Procesos | 10 | 8 | 7 | 70% | 🟢 |
| Reglas | 13 | 10 | 9 | 69% | 🟢 |
| Excepciones | 10 | 7 | 5 | 50% | 🟡 |
| Decisiones | 6 | 5 | 5 | 83% | 🟢 |
| KPIs | 7 | 5 | 4 | 57% | 🟢 |
| Automatizaciones | 8 | 3 | 0 | 0% | ⚪ |

> **Nota:** Los números son estimaciones iniciales. Se ajustarán durante la KES-01.

---

## 5. Criterios de cierre por categoría

| Categoría | Umbral de cierre | Justificación |
|-----------|------------------|---------------|
| Términos | 100% | Sin vocabulario común, todo lo demás es ambiguo. |
| Actores | 100% | Debe conocerse quién participa. |
| Objetos | ≥ 90% | El modelo de datos depende de esto. |
| Eventos | ≥ 90% | El Event Bus se alimenta de eventos. |
| Procesos | ≥ 80% | Basta con los procesos principales. |
| Reglas | ≥ 90% | Reglas críticas no pueden faltar. |
| Excepciones | ≥ 70% | Es imposible conocer todas, pero las principales sí. |
| Decisiones | ≥ 80% | Las decisiones clave deben estar claras. |
| KPIs | ≥ 70% | Pueden refinarse con el tiempo. |
| Automatizaciones | ≥ 50% | Lista inicial de oportunidades. |

---

## 6. Cálculo de cobertura

```text
Cobertura = (Ítems validados / Ítems esperados) × 100
```

Solo cuentan los ítems **validados**. Los capturados pero no validados (hipótesis) no suman.

---

## 7. Registro de avance por KES

| KES | Dominio | Fecha | Cobertura antes | Cobertura después | Estado |
|-----|---------|-------|-----------------|-------------------|--------|
| KES-Pilot | Metodología / Almacén | 2026-06-26 | 0% | 65% | ✅ Completada |
| KES-0 | Lenguaje Empresarial | — | 0% | — | Programada |
| KES-01 | Almacén | — | 0% | — | Programada |
| KES-02 | Compras | — | 0% | — | Pendiente |
| KES-03 | Logística | — | 0% | — | Pendiente |
| KES-04 | Calidad | — | 0% | — | Pendiente |
| KES-05 | Ventas | — | 0% | — | Pendiente |
| KES-06 | Contabilidad | — | 0% | — | Pendiente |
| KES-07 | RRHH | — | 0% | — | Pendiente |
| KES-08 | Inteligencia Empresarial | — | 0% | — | Pendiente |
| KES-09 | Dirección y transversales | — | 0% | — | Pendiente |

---

## 8. Producto final esperado

Al finalizar todas las KES, esta matriz debe mostrar:

- Todos los dominios en verde (✅) en categorías críticas.
- Conocimiento pendiente explícitamente identificado.
- Nivel de confianza promedio por dominio.

---

## Historial de cambios

| Fecha | Versión | Cambio |
|-------|---------|--------|
| 2026-06-25 | 0.1.0 | Creación de la Knowledge Coverage Matrix con plantilla por dominio y categoría. |
| 2026-06-25 | 0.2.0 | Agregado dominio D0 Lenguaje Empresarial, columna de Términos y KES-0. |
| 2026-06-25 | 0.3.0 | Agregado KES-Pilot al registro de avance. |
