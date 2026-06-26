# Catálogo de Decisiones — CJ_OS

**Versión:** 0.1.0  
**Fecha:** 2026-06-25  
**Estado:** Borrador inicial — pendiente de M2.8 BKA  
**Propósito:** Documentar las decisiones reales que ocurren en cada dominio de 3P: qué información necesitan, quién las toma, qué resultados pueden tener y cuánta autonomía puede tener CJ_OS.

---

## 1. ¿Qué es una decisión en CJ_OS?

Las empresas realmente no son procesos. Son decisiones. Cada decisión:

- Se toma en un contexto.
- Requiere información.
- Tiene opciones posibles.
- Tiene un responsable.
- Genera consecuencias.

> **El Catálogo de Decisiones será la base del Motor de Decisiones de CJ_OS.**

---

## 2. Formato del catálogo

Cada decisión incluye:

- **Pregunta:** ¿qué se decide?
- **Dominio:** ¿a qué área pertenece?
- **Información necesaria:** ¿qué datos se requieren?
- **Opciones:** ¿qué resultados son posibles?
- **Responsable:** ¿quién decide?
- **Autonomía de CJ_OS:** A0-A5.
- **Evento asociado:** ¿qué evento dispara o registra la decisión?
- **Consecuencias:** ¿qué pasa después?

---

## 3. Decisiones por dominio

### D4 — Almacén

#### D4.1 ¿Aceptar la mercancía recibida?

| Campo | Valor |
|-------|-------|
| **Pregunta** | ¿Se acepta la recepción completa, parcial o se rechaza? |
| **Dominio** | Almacén |
| **Información necesaria** | OC, proveedor, cantidad pedida, cantidad recibida, estado físico, evidencia fotográfica. |
| **Opciones** | Aceptar completa / Aceptar parcial / Rechazar / Retener para calidad. |
| **Responsable** | Jefe de Almacén + Jefe de Calidad (si aplica). |
| **Autonomía CJ_OS** | A1: recomienda opción basada en comparación OC vs. físico. |
| **Evento asociado** | `llego_mercancia`, `se_recibio_oc`. |
| **Consecuencias** | Actualiza existencia, genera NC, notifica a compras/proveedor. |

#### D4.2 ¿Aplicar merma?

| Campo | Valor |
|-------|-------|
| **Pregunta** | ¿Se registra como merma el producto dañado/caducado? |
| **Dominio** | Almacén |
| **Información necesaria** | Producto, cantidad, causa, evidencia fotográfica, ubicación, responsable. |
| **Opciones** | Aplicar merma / Rechazar solicitud / Investigar más. |
| **Responsable** | Jefe de Almacén / Director según monto. |
| **Autonomía CJ_OS** | A4: propone ajuste con evidencia; espera aprobación. |
| **Evento asociado** | `se_detecto_merma`. |
| **Consecuencias** | Reduce existencia, genera ajuste, actualiza KPIs. |

#### D4.3 ¿Cerrar inventario con diferencias?

| Campo | Valor |
|-------|-------|
| **Pregunta** | ¿Se cierra el conteo y se aplican ajustes? |
| **Dominio** | Almacén |
| **Información necesaria** | Cantidad física, cantidad sistema, diferencias, causa, responsable. |
| **Opciones** | Cerrar con ajustes / Recontar / Investigar. |
| **Responsable** | Jefe de Almacén. |
| **Autonomía CJ_OS** | A4: propone ajustes; espera aprobación. |
| **Evento asociado** | `se_cerro_inventario`. |
| **Consecuencias** | Actualiza existencias, genera alerta si discrepancia alta. |

#### D4.4 ¿Reordenar producto?

| Campo | Valor |
|-------|-------|
| **Pregunta** | ¿Se genera una orden de compra de reposición? |
| **Dominio** | Almacén / Compras |
| **Información necesaria** | Stock actual, stock mínimo, punto de reorden, lead time, demanda reciente, proveedor. |
| **Opciones** | Sí / No / Diferente cantidad / Diferente proveedor. |
| **Responsable** | Comprador / Director según monto. |
| **Autonomía CJ_OS** | A1: recomienda OC; A3 si monto y proveedor están preautorizados. |
| **Evento asociado** | `stock_bajo_detectado`. |
| **Consecuencias** | Crea solicitud de compra o OC. |

#### D4.5 ¿Cambiar ubicación de producto?

| Campo | Valor |
|-------|-------|
| **Pregunta** | ¿Se traslada producto a otro rack? |
| **Dominio** | Almacén |
| **Información necesaria** | Producto, ubicación origen, ubicación destino, motivo, capacidad destino. |
| **Opciones** | Mover / No mover. |
| **Responsable** | Jefe de Almacén. |
| **Autonomía CJ_OS** | A2/A3: ejecuta transferencia si está dentro de política. |
| **Evento asociado** | Transferencia generada. |
| **Consecuencias** | Actualiza existencias por ubicación. |

### D3 — Compras

#### D3.1 ¿Aprobar orden de compra?

| Campo | Valor |
|-------|-------|
| **Pregunta** | ¿Se autoriza la OC? |
| **Información necesaria** | Proveedor, productos, cantidades, precio, total, presupuesto disponible. |
| **Opciones** | Aprobar / Rechazar / Modificar. |
| **Responsable** | Comprador (dentro de presupuesto) / Director (mayor a umbral). |
| **Autonomía CJ_OS** | A1: recomienda aprobación; A3 si está dentro de reglas predefinidas. |
| **Evento asociado** | `se_creo_oc`. |
| **Consecuencias** | OC enviada o rechazada. |

#### D3.2 ¿Cambiar de proveedor?

| Campo | Valor |
|-------|-------|
| **Pregunta** | ¿Se selecciona otro proveedor para una compra? |
| **Información necesaria** | Precios, lead time, calidad histórica, disponibilidad. |
| **Opciones** | Proveedor A / B / C. |
| **Responsable** | Comprador / Director. |
| **Autonomía CJ_OS** | A1: recomienda según score de proveedor. |
| **Evento asociado** | `se_creo_cotizacion`. |
| **Consecuencias** | OC asignada a proveedor seleccionado. |

### D6 — Calidad

#### D6.1 ¿Retener o liberar lote?

| Campo | Valor |
|-------|-------|
| **Pregunta** | ¿El lote pasa inspección o se retiene? |
| **Información necesaria** | Estándar de calidad, resultado de inspección, evidencia. |
| **Opciones** | Liberar / Retener / Rechazar. |
| **Responsable** | Jefe de Calidad. |
| **Autonomía CJ_OS** | A4: propone según inspección; espera aprobación. |
| **Evento asociado** | `inspeccion_programada`. |
| **Consecuencias** | Lote disponible o bloqueado. |

### D2 — Ventas

#### D2.1 ¿Aprobar descuento especial?

| Campo | Valor |
|-------|-------|
| **Pregunta** | ¿Se aplica descuento fuera de política? |
| **Información necesaria** | Cliente, historial, pedido, margen, política vigente. |
| **Opciones** | Aprobar / Rechazar / Negociar. |
| **Responsable** | Gerente Comercial / Director. |
| **Autonomía CJ_OS** | A1: recomienda; A2 si está dentro de política. |
| **Evento asociado** | `descuento_solicitado`. |
| **Consecuencias** | Pedido con descuento aplicado o rechazado. |

### D7 — Contabilidad

#### D7.1 ¿Programar pago a proveedor?

| Campo | Valor |
|-------|-------|
| **Pregunta** | ¿Se paga al proveedor y en qué fecha? |
| **Información necesaria** | OC, factura, fecha vencimiento, flujo de efectivo, monto. |
| **Opciones** | Pagar hoy / Programar / Retener. |
| **Responsable** | Contador / Director según monto. |
| **Autonomía CJ_OS** | A1: recomiende fecha óptima; A3 si está dentro de flujo aprobado. |
| **Evento asociado** | `pago_programado`. |
| **Consecuencias** | Egreso registrado. |

---

## 4. Decisiones transversales

| Pregunta | Información necesaria | Responsable | Autonomía CJ_OS | Evento |
|----------|----------------------|-------------|-----------------|--------|
| ¿Escalar situación a Dirección? | Severidad, impacto, regla violada. | Sistema / Jefe de área. | A5: escala automáticamente. | `excepcion_detectada` |
| ¿Activar modo offline? | Estado de conectividad, criticidad de operación. | Sistemas / CJ_OS. | A2/A3: activa según política. | `modo_offline_activado` |
| ¿Generar reporte ejecutivo? | Datos disponibles, frecuencia, destinatarios. | Analista / CJ_OS. | A2: genera programado. | `reporte_solicitado` |

---

## 5. Criterios de aprobación

- [ ] Cada decisión tiene pregunta, información, opciones y responsable.
- [ ] Cada decisión tiene nivel de autonomía A0-A5 asignado.
- [ ] Cada decisión está vinculada a un evento.
- [ ] Carlos valida que las decisiones reflejan la operación real.

---

## Historial de cambios

| Fecha | Versión | Cambio |
|-------|---------|--------|
| 2026-06-25 | 0.1.0 | Creación del Catálogo de Decisiones con decisiones iniciales de Almacén y dominios clave. |
