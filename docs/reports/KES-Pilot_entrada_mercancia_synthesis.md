# Síntesis KES-Pilot — Entrada de mercancía de proveedor

**Fecha:** 2026-06-26  
**Proceso:** Entrada de mercancía de proveedor y asignación a sub-almacenes  
**Dominio:** Almacén / Compras / Logística / Calidad  
**Entrevistado:** Carlos (Product Owner)  
**Documento fuente:** `docs/reports/KES-Pilot_entrada_mercancia.md`

---

## 1. Conclusión de la KES-Pilot

La metodología KES funcionó. En una sola sesión se logró capturar el proceso real de entrada de mercancía en 3P, incluyendo actores, eventos, reglas, decisiones, excepciones y KPIs. El proceso **no es lineal ideal**: la entrada se registra en SAE por Logística, pero el control físico y distribución a sub-almacenes se hace en Excel.

**Resultado:** La metodología está lista para escalar a KES-0 y KES-01.

---

## 2. Proceso validado (flujo real)

```text
Proveedor notifica envío
        ↓
Logística/Compras avisa a Almacén
        ↓
Llega transporte → Almacén recibe físicamente
        ↓
Almacén cuenta, inspecciona, toma fotos
        ↓
Almacén entrega reporte + factura firmada a Logística
        ↓
Logística registra entrada en SAE
        ↓
SAE actualiza existencias automáticamente
        ↓
Jefe de Almacén asigna sub-almacén por proveedor
        ↓
Se genera vale de entrada y se actualiza Excel (sub-almacén + Mini-SAE)
```

---

## 3. Hallazgos clave

### 3.1 Roles
- **Logística y Compras** es el mismo puesto en 3P.
- **Almacén** solo recibe, cuenta e inspecciona. No captura en SAE.
- **Logística** tiene la última palabra sobre discrepancias (junto con Gerencia).

### 3.2 Sistemas
- **SAE** es el sistema oficial de entradas y existencias generales.
- **Excel de almacén** es el control operativo de sub-almacenes.
- **Desconexión conocida:** Excel y SAE no siempre coinciden. Se corrigen con ajustes manuales.

### 3.3 Sub-almacenes
- Cada sub-almacén está asociado a un proveedor.
- Un producto puede estar en varios sub-almacenes si varios proveedores lo surten.
- Producto nuevo → se asigna al sub-almacén de su proveedor.

### 3.4 Conteo e inspección
- Se toman fotos en cada recepción.
- Productos líquidos (detergentes) y frágiles requieren revisión especial.
- Cuarentena: 1-2 días máximo.

### 3.5 Excepciones más frecuentes
1. Material faltante.
2. Material sobrante.
3. Producto dañado (se acepta parcialmente y Logística arregla con proveedor).
4. Excedente de envío: se queda y se pide factura del sobrante.

---

## 4. Eventos confirmados

| Evento | Descripción |
|--------|-------------|
| `llego_mercancia` | El transporte llegó al almacén. |
| `se_inicio_recepcion` | Almacén comienza conteo e inspección. |
| `se_registro_entrada_en_sae` | Logística capturó la entrada en SAE. |
| `se_detecto_faltante` | Cantidad recibida menor a la esperada. |
| `se_detecto_sobrante` | Cantidad recibida mayor a la esperada. |
| `se_detecto_dano` | Producto o empaque dañado. |
| `mercancia_aprobada` | Se acepta la recepción. |
| `mercancia_rechazada` | Se rechaza material. |
| `se_asigno_subalmacen` | Se decide sub-almacén destino. |
| `se_genero_vale_entrada` | Se registra movimiento de entrada. |
| `se_actualizo_existencia` | Se actualiza stock en sub-almacén/Mini-SAE. |

---

## 5. Reglas validadas

| # | Regla | Responsable |
|---|-------|-------------|
| R1 | Toda entrada requiere OC o factura. | Logística |
| R2 | Almacén no registra en SAE; solo recibe, cuenta e informa. | Almacén |
| R3 | Fotografía obligatoria en cada recepción. | Almacén |
| R4 | Discrepancias se reportan a Logística. | Almacén → Logística |
| R5 | Sub-almacén se asigna por proveedor. | Jefe de Almacén |
| R6 | Mini-SAE debe reflejar suma de sub-almacenes. | Jefe de Almacén |
| R7 | Excel se actualiza diariamente. | Jefe de Almacén |

---

## 6. Decisiones confirmadas

| Decisión | Responsable |
|----------|-------------|
| ¿Aceptar mercancía con discrepancia? | Logística / Gerencia |
| ¿Aplicar merma? | Logística / Gerencia |
| ¿Asignar sub-almacén a producto nuevo? | Jefe de Almacén |
| ¿Mandar a cuarentena? | Inspector de Calidad / Jefe de Almacén |

---

## 7. Oportunidades de automatización detectadas

1. **Alerta de entrada pendiente:** Cuando Logística registra entrada en SAE, avisar a Almacén para asignar sub-almacén.
2. **Reconciliación automática:** Comparar existencias de SAE vs. suma de sub-almacenes y reportar diferencias.
3. **Asignación sugerida de sub-almacén:** Basada en proveedor del producto.
4. **Detección de excedentes/faltantes:** Al comparar OC/factura vs. conteo físico.
5. **Recordatorio de cuarentena:** Si material lleva más de 2 días en cuarentena, notificar.

---

## 8. Términos para el Business Dictionary

- **Sub-almacén:** Ubicación lógica de inventario asociada a un proveedor.
- **Cantidad viva:** Lo que queda por facturar/vender de un vale de salida.
- **Logística y Compras:** Puesto combinado en 3P responsable de compras nacionales e internacionales y registro de entradas en SAE.
- **Recepción:** Acción física de recibir, contar e inspeccionar mercancía.
- **Cuarentena:** Estado temporal de mercancía en espera de inspección o decisión.

---

## 9. Próximos pasos

1. **Actualizar Business Dictionary** con los términos validados.
2. **Actualizar Knowledge Coverage Matrix** con cobertura de Almacén tras KES-Pilot.
3. **Iniciar diseño del conector SAE → CJ_OS** para leer entradas de mercancía.
4. **Iniciar diseño del conector Excel de almacén** para sincronizar sub-almacenes.

---

*Síntesis generada automáticamente por CJ_OS el 2026-06-26.*
