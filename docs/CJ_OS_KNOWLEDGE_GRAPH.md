# Knowledge Graph — CJ_OS

**Versión:** 0.1.0  
**Fecha:** 2026-06-25  
**Estado:** Borrador inicial — pendiente de M2.8 BKA  
**Propósito:** Documentar las relaciones entre entidades de 3P. Será la base para el diseño de relaciones en PostgreSQL y para la navegación de agentes de IA.

---

## 1. ¿Qué es el Knowledge Graph?

El Knowledge Graph es un documento que describe la red de conocimiento de la empresa en forma de tripletas:

```text
Sujeto ──Relación──► Objeto
```

Ejemplo:

```text
Producto ──se almacena en──► Rack
```

No es código. No es una base de datos. Es el **mapa semántico** que CJ_OS necesita para entender cómo se conectan las cosas en 3P.

---

## 2. Formato de las tripletas

Cada relación incluye:

- **Sujeto:** la entidad origen.
- **Relación:** el verbo que las conecta.
- **Objeto:** la entidad destino.
- **Cardinalidad:** 1:1, 1:N, N:M.
- **Tipo de relación:** composición, agregación, referencia.
- **Ejemplo real de 3P.**

---

## 3. Knowledge Graph por dominio

### D4 — Almacén

| Sujeto | Relación | Objeto | Cardinalidad | Tipo | Ejemplo real |
|--------|----------|--------|--------------|------|--------------|
| Producto | se almacena en | Rack | N:M | Referencia | Tornillo SKU-001 está en Rack A-12. |
| Producto | pertenece a | Proveedor | N:1 | Referencia | SKU-001 pertenece a Proveedor X. |
| Producto | tiene | Existencia | 1:N | Composición | SKU-001 tiene existencia en Rack A-12 y B-03. |
| Existencia | se encuentra en | Ubicación | 1:1 | Composición | La existencia de SKU-001 está en A-12. |
| Vale | consume/produce | Producto | 1:N | Agregación | Vale #100 consume 50 SKU-001. |
| Inventario | contiene | Producto | 1:N | Agregación | Inventario ciclico de tornillos contiene SKU-001. |
| Merma | afecta | Existencia | 1:1 | Agregación | Merma #20 afecta existencia de SKU-001 en A-12. |
| OC | genera | Entrada | 1:N | Agregación | OC #500 genera entrada #E-100. |
| Entrada | actualiza | Existencia | 1:N | Agregación | Entrada #E-100 aumenta existencia de SKU-001. |
| Pedido | genera | Salida | 1:N | Agregación | Pedido #P-200 genera salida #S-150. |
| Salida | actualiza | Existencia | 1:N | Agregación | Salida #S-150 reduce existencia de SKU-001. |
| Transferencia | mueve | Existencia | 1:1 | Agregación | Transferencia #T-30 mueve SKU-001 de A-12 a B-03. |
| Evidencia fotográfica | pertenece a | Vale | N:1 | Referencia | Foto #F-1 pertenece a Vale #100. |
| Evidencia fotográfica | pertenece a | Merma | N:1 | Referencia | Foto #F-2 pertenece a Merma #20. |
| Producto | es | Material indirecto | 1:1 (subtipo) | Especialización | Cinta adhesiva es material indirecto. |
| Rack | tiene | Capacidad | 1:1 | Atributo | Rack A-12 soporta 500 kg. |
| Rack | permite | Familia de producto | N:M | Referencia | Rack A-12 permite familias metales y tornillos. |

### D3 — Compras

| Sujeto | Relación | Objeto | Cardinalidad | Tipo | Ejemplo real |
|--------|----------|--------|--------------|------|--------------|
| Proveedor | recibe | OC | 1:N | Agregación | Proveedor X recibe OC #500. |
| OC | contiene | Producto | 1:N | Composición | OC #500 contiene SKU-001 y SKU-002. |
| OC | genera | Entrada | 1:N | Agregación | OC #500 genera entrada #E-100. |
| Proveedor | tiene | Evaluación | 1:N | Agregación | Proveedor X tiene evaluación trimestral. |
| Solicitud de compra | origina | OC | 1:1 | Agregación | Solicitud #SC-10 origina OC #500. |

### D2 — Ventas

| Sujeto | Relación | Objeto | Cardinalidad | Tipo | Ejemplo real |
|--------|----------|--------|--------------|------|--------------|
| Cliente | realiza | Pedido | 1:N | Agregación | Cliente Y realiza pedido #P-200. |
| Pedido | contiene | Producto | 1:N | Composición | Pedido #P-200 contiene SKU-001. |
| Pedido | genera | Salida | 1:N | Agregación | Pedido #P-200 genera salida #S-150. |
| Pedido | genera | Factura | 1:1 | Agregación | Pedido #P-200 genera factura #F-300. |
| Cliente | tiene | Lista de precios | 1:1 | Referencia | Cliente Y tiene lista mayoreo. |

### D5 — Logística

| Sujeto | Relación | Objeto | Cardinalidad | Tipo | Ejemplo real |
|--------|----------|--------|--------------|------|--------------|
| Pedido | se envía mediante | Envío | 1:N | Agregación | Pedido #P-200 se envía en envío #E-400. |
| Envío | usa | Transportista | N:1 | Referencia | Envío #E-400 usa Transportista Z. |
| Envío | tiene | Guía | 1:1 | Composición | Envío #E-400 tiene guía #G-500. |
| Envío | pertenece a | Ruta | N:1 | Agregación | Envío #E-400 pertenece a Ruta Norte. |
| Cliente | recibe | Envío | 1:N | Agregación | Cliente Y recibe envío #E-400. |

### D6 — Calidad

| Sujeto | Relación | Objeto | Cardinalidad | Tipo | Ejemplo real |
|--------|----------|--------|--------------|------|--------------|
| Lote | es inspeccionado por | Inspección | 1:N | Agregación | Lote L-100 es inspeccionado. |
| Inspección | genera | No conformidad | 1:N | Agregación | Inspección genera NC #NC-10. |
| No conformidad | requiere | Acción correctiva | 1:1 | Agregación | NC #NC-10 requiere AC #AC-5. |
| Proveedor | genera | No conformidad | 1:N | Agregación | Proveedor X generó NC #NC-10. |

### D7 — Contabilidad

| Sujeto | Relación | Objeto | Cardinalidad | Tipo | Ejemplo real |
|--------|----------|--------|--------------|------|--------------|
| Pedido | genera | Factura | 1:1 | Agregación | Pedido #P-200 genera factura #F-300. |
| Factura | genera | Pago | 1:N | Agregación | Factura #F-300 recibe pago #PA-600. |
| Cliente | debe | Cuenta por cobrar | 1:N | Agregación | Cliente Y debe cuenta #CC-700. |
| Proveedor | se le debe | Cuenta por pagar | 1:N | Agregación | Proveedor X tiene cuenta #CP-800. |
| Empleado | recibe | Nómina | 1:N | Agregación | Empleado recibe nómina #N-900. |

### D8 — RRHH

| Sujeto | Relación | Objeto | Cardinalidad | Tipo | Ejemplo real |
|--------|----------|--------|--------------|------|--------------|
| Empleado | tiene | Expediente | 1:1 | Composición | Francisco tiene expediente #EXP-1. |
| Empleado | registra | Asistencia | 1:N | Agregación | Francisco registra asistencia diaria. |
| Empleado | solicita | Permiso | 1:N | Agregación | Francisco solicita permiso #PER-2. |
| Empleado | asiste a | Capacitación | N:M | Agregación | Francisco asiste a capacitación de seguridad. |

### D9 — Inteligencia Empresarial

| Sujeto | Relación | Objeto | Cardinalidad | Tipo | Ejemplo real |
|--------|----------|--------|--------------|------|--------------|
| KPI | mide | Proceso | N:1 | Referencia | KPI "precisión de inventario" mide inventarios. |
| Reporte | contiene | KPI | 1:N | Composición | Reporte ejecutivo contiene 5 KPIs. |
| Alerta | se dispara por | KPI | N:1 | Referencia | Alerta de stock bajo se dispara por KPI. |
| Dashboard | muestra | Reporte | 1:N | Agregación | Dashboard de dirección muestra reportes. |

---

## 4. Grafo visual resumido (Almacén)

```text
Producto ──se almacena en──► Rack
    │                            │
    ├── pertenece a ────────────► Proveedor
    │
    ├── tiene ──────────────────► Existencia ──se encuentra en──► Ubicacion
    │
    ├── consume/produce ◄──────── Vale
    │
    ├── contiene ◄────────────── Inventario
    │
    └── es ◄──────────────────── Material indirecto

OC ──genera──► Entrada ──actualiza──► Existencia
Pedido ──genera──► Salida ──actualiza──► Existencia
Merma ──afecta──► Existencia
Transferencia ──mueve──► Existencia entre Ubicaciones
Evidencia fotográfica ──pertenece a──► Vale / Merma / Inventario
```

---

## 5. Criterios de aprobación

- [ ] Todas las entidades del dominio están representadas.
- [ ] Cada relación tiene cardinalidad y tipo definidos.
- [ ] No hay relaciones ambiguas.
- [ ] El grafo puede leerse como input para el Modelo de Datos.
- [ ] Carlos valida que las relaciones reflejan la realidad de 3P.

---

## Historial de cambios

| Fecha | Versión | Cambio |
|-------|---------|--------|
| 2026-06-25 | 0.1.0 | Creación del Knowledge Graph con tripletas por dominio, usando Almacén como patrón. |
