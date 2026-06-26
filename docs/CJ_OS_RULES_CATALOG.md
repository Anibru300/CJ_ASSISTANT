# Catálogo de Reglas — CJ_OS

**Versión:** 0.1.0  
**Fecha:** 2026-06-25  
**Estado:** Borrador inicial — pendiente de M2.8 BKA  
**Propósito:** Documentar las reglas de negocio de 3P de forma explícita, separada y accionable. Cada regla será una futura validación automática en CJ_OS.

---

## 1. ¿Qué es una regla de negocio?

Una regla es una restricción o comportamiento que debe cumplirse en la operación. En CJ_OS, las reglas:

- Son expresables como validaciones automáticas.
- Tienen tipo, prioridad y evento relacionado.
- Indican si pueden romperse y quién puede autorizar una excepción.

> **Este catálogo será la fuente de las políticas del Core de CJ_OS.**

---

## 2. Formato del catálogo

Cada regla incluye:

- **ID:** código único.
- **Nombre:** breve y descriptivo.
- **Dominio:** a qué área pertenece.
- **Tipo:** integridad, autorización, flujo, excepción, auditoría.
- **Prioridad:** alta, media, baja.
- **Descripción:** qué dice la regla.
- **¿Se puede romper?** sí / no.
- **Quién autoriza excepción:** rol o "nadie".
- **Evento relacionado:** qué evento la activa o verifica.
- **Autonomía CJ_OS:** A0-A5.

---

## 3. Reglas por dominio

### D4 — Almacén

| ID | Nombre | Tipo | Prioridad | Descripción | ¿Se puede romper? | Autoriza excepción | Evento relacionado | Autonomía |
|----|--------|------|-----------|-------------|-------------------|--------------------|--------------------|-----------|
| R-D4-001 | Existencia nunca negativa | Integridad | Alta | La cantidad física de un producto nunca puede ser menor a cero. | No | Nadie | `ajuste_inventario`, `se_cerro_vale` | A5 |
| R-D4-002 | Vale cerrado no se modifica | Integridad | Alta | Un vale en estado cerrado no puede editarse; debe revertirse. | No | Nadie | `se_modifico_vale` | A5 |
| R-D4-003 | Inventarios históricos no se eliminan | Integridad | Alta | Los registros de inventarios cerrados no pueden borrarse. | No | Nadie | `se_cerro_inventario` | A5 |
| R-D4-004 | Merma requiere evidencia | Flujo | Alta | Toda merma debe tener evidencia fotográfica y causa documentada. | No | Nadie | `se_detecto_merma` | A4 |
| R-D4-005 | Entrada requiere proveedor | Integridad | Media | Toda entrada de mercancía debe estar vinculada a un proveedor o OC. | Con autorización | Director | `llego_mercancia` | A4 |
| R-D4-006 | Salida requiere responsable | Integridad | Media | Toda salida de mercancía debe tener responsable y motivo. | No | Nadie | `se_creo_vale` | A2 |
| R-D4-007 | Modificación importante auditada | Auditoría | Alta | Toda modificación a datos críticos debe quedar registrada. | No | Nadie | `se_modifico_vale` | A2-A5 |
| R-D4-008 | Disponibilidad suficiente para salida | Integridad | Alta | No se puede surtir un pedido si no hay stock disponible. | No | Nadie | `se_creo_vale` | A5 |
| R-D4-009 | Comprometido no mayor a físico | Integridad | Alta | El stock comprometido no puede superar la existencia física. | No | Nadie | `se_creo_vale` | A5 |
| R-D4-010 | Picking reabastecido antes de agotarse | Flujo | Media | Las ubicaciones de picking deben reabastecerse antes de llegar a cero. | No | Nadie | `stock_bajo_detectado` | A1/A2 |
| R-D4-011 | Rack no excede capacidad | Integridad | Media | Una ubicación no puede recibir más producto del que soporta. | No | Nadie | `llego_mercancia` | A5 |
| R-D4-012 | Productos incompatibles no se mezclan | Integridad | Alta | No se pueden ubicar juntos productos incompatibles (ej. químicos, temperatura). | No | Nadie | `llego_mercancia` | A4 |
| R-D4-013 | Material indirecto no afecta ventas | Flujo | Media | Los movimientos de material indirecto no generan facturación. | No | Nadie | `se_creo_vale` | A2 |

### D3 — Compras

| ID | Nombre | Tipo | Prioridad | Descripción | ¿Se puede romper? | Autoriza excepción | Evento relacionado | Autonomía |
|----|--------|------|-----------|-------------|-------------------|--------------------|--------------------|-----------|
| R-D3-001 | OC requiere proveedor autorizado | Integridad | Alta | Solo se pueden generar OC a proveedores dados de alta. | Con autorización | Director | `se_creo_oc` | A4 |
| R-D3-002 | OC mayor a umbral requiere aprobación | Autorización | Alta | Las OC que superen el monto límite requieren aprobación del Director. | Sí | Director | `se_creo_oc` | A4 |
| R-D3-003 | OC cancelada no se recibe | Flujo | Alta | No se puede registrar entrada contra una OC cancelada. | No | Nadie | `se_recibio_oc` | A5 |
| R-D3-004 | Recepción debe coincidir con OC | Integridad | Alta | La entrada debe coincidir con OC o estar justificada. | Con autorización | Jefe de Almacén + Comprador | `se_recibio_oc` | A4 |

### D6 — Calidad

| ID | Nombre | Tipo | Prioridad | Descripción | ¿Se puede romper? | Autoriza excepción | Evento relacionado | Autonomía |
|----|--------|------|-----------|-------------|-------------------|--------------------|--------------------|-----------|
| R-D6-001 | Lote retenido no se libera sin calidad | Autorización | Alta | Un lote retenido solo puede liberarse por Jefe de Calidad. | No | Nadie | `lote_liberado` | A4 |
| R-D6-002 | NC requiere causa y AC | Flujo | Alta | Toda no conformidad debe tener causa identificada y acción correctiva. | No | Nadie | `no_conformidad_detectada` | A4 |
| R-D6-003 | Auditorías programadas y cerradas | Flujo | Media | Las auditorías deben tener programa, ejecución y cierre documentado. | No | Nadie | `auditoria_realizada` | A3 |

### D2 — Ventas

| ID | Nombre | Tipo | Prioridad | Descripción | ¿Se puede romper? | Autoriza excepción | Evento relacionado | Autonomía |
|----|--------|------|-----------|-------------|-------------------|--------------------|--------------------|-----------|
| R-D2-001 | Pedido requiere cliente registrado | Integridad | Alta | No se puede crear un pedido sin cliente en el sistema. | No | Nadie | `pedido_creado` | A5 |
| R-D2-002 | Descuento fuera de política requiere aprobación | Autorización | Alta | Descuentos que excedan la política requieren aprobación. | Sí | Gerente Comercial / Director | `descuento_solicitado` | A4 |
| R-D2-003 | No facturar sin stock comprometido | Flujo | Alta | No se puede facturar un pedido sin stock reservado o surtido. | No | Nadie | `pedido_facturado` | A5 |

### D7 — Contabilidad

| ID | Nombre | Tipo | Prioridad | Descripción | ¿Se puede romper? | Autoriza excepción | Evento relacionado | Autonomía |
|----|--------|------|-----------|-------------|-------------------|--------------------|--------------------|-----------|
| R-D7-001 | Egreso mayor a umbral requiere aprobación | Autorización | Alta | Pagos que superen el umbral requieren aprobación del Director. | Sí | Director | `pago_programado` | A4 |
| R-D7-002 | Factura ligada a pedido o servicio | Integridad | Alta | Toda factura debe estar vinculada a un pedido o servicio prestado. | Con autorización | Contador | `factura_emitida` | A4 |
| R-D7-003 | Nómina requiere asistencia validada | Flujo | Alta | El cálculo de nómina requiere asistencia del período. | No | Nadie | `nomina_generada` | A3 |

### D8 — RRHH

| ID | Nombre | Tipo | Prioridad | Descripción | ¿Se puede romper? | Autoriza excepción | Evento relacionado | Autonomía |
|----|--------|------|-----------|-------------|-------------------|--------------------|--------------------|-----------|
| R-D8-001 | Baja requiere aprobación | Autorización | Alta | Toda baja de empleado requiere aprobación. | Sí | Director | `empleado_dado_de_baja` | A4 |
| R-D8-002 | Modificación salarial requiere aprobación | Autorización | Alta | Cambios de salario requieren aprobación del Director. | Sí | Director | `modificacion_salarial` | A4 |
| R-D8-003 | Documentación completa para alta | Flujo | Media | Un empleado no debe quedar dado de alta sin expediente completo. | Con autorización | Jefe de RRHH | `empleado_contratado` | A3 |

---

## 4. Reglas transversales

| ID | Nombre | Tipo | Prioridad | Descripción | ¿Se puede romper? | Autoriza excepción | Evento relacionado | Autonomía |
|----|--------|------|-----------|-------------|-------------------|--------------------|--------------------|-----------|
| R-TRV-001 | Veto humano siempre disponible | Autorización | Alta | Todo humano con autoridad puede anular una decisión de CJ_OS. | Sí | Humano con permiso | Cualquier decisión | A5 |
| R-TRV-002 | Toda decisión importante explicable | Auditoría | Alta | CJ_OS debe poder explicar por qué tomó una decisión. | No | Nadie | Cualquier decisión | A0-A5 |
| R-TRV-003 | Nunca perder información | Integridad | Alta | CJ_OS no debe eliminar información crítica; solo marcar como obsoleta. | No | Nadie | Cualquier evento | A5 |
| R-TRV-004 | Modo offline disponible | Excepción | Media | Si falla conectividad, CJ_OS debe permitir operación offline y sincronizar después. | Sí | Sistemas | `modo_offline_activado` | A2 |

---

## 5. Criterios de aprobación

- [ ] Cada regla tiene ID único, tipo, prioridad y descripción clara.
- [ ] Se indica si la regla es rompible y quién autoriza la excepción.
- [ ] Cada regla está vinculada a un evento.
- [ ] Las reglas son expresables como validaciones en código.
- [ ] Carlos valida que las reglas representan políticas reales de 3P.

---

## Historial de cambios

| Fecha | Versión | Cambio |
|-------|---------|--------|
| 2026-06-25 | 0.1.0 | Creación del Catálogo de Reglas con reglas iniciales por dominio y transversales. |
