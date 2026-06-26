# Catálogo de Eventos — CJ_OS

**Versión:** 0.1.0  
**Fecha:** 2026-06-25  
**Estado:** Borrador inicial — pendiente de M2.8 BKA  
**Propósito:** Documentar todos los eventos de negocio que alimentarán el Event Bus, los workflows de n8n, los agentes de IA, los logs y las automatizaciones.

---

## 1. ¿Qué es un evento?

Un evento es algo que ocurre en la empresa y que CJ_OS necesita conocer. Todo evento:

- Tiene un nombre en formato `sustantivo_verbo`.
- Tiene un disparador.
- Lleva información (payload).
- Puede ser consumido por uno o más procesos.

> **CJ_OS vive por eventos.** Un flujo no empieza con un botón; empieza con un evento.

---

## 2. Formato del catálogo

Cada evento incluye:

- **Nombre:** `sustantivo_verbo` en minúsculas y snake_case.
- **Dominio:** a qué dominio pertenece.
- **Disparador:** qué lo genera.
- **Payload:** información que transporta.
- **Proceso que lo genera:** quién lo produce.
- **Procesos que lo consumen:** quién reacciona ante él.
- **Autonomía típica de CJ_OS:** A0-A5.

---

## 3. Eventos por dominio

### D4 — Almacén

| Evento | Disparador | Payload | Generado por | Consumido por | Autonomía |
|--------|------------|---------|--------------|---------------|-----------|
| `llego_mercancia` | Proveedor entrega físicamente. | proveedor, oc, productos, cantidades, foto | Entrada de mercancía | Recepción, calidad, notificaciones | A0/A1 |
| `se_creo_vale` | Usuario inicia movimiento. | tipo, folio, responsable, lineas | Entrada, salida, transferencia, ajuste, merma | Auditoría, inventario | A2 |
| `se_modifico_vale` | Usuario corrige antes de cerrar. | folio, cambios, usuario | Vale abierto | Auditoría | A2 |
| `se_cerro_vale` | Vale validado y afecta stock. | folio, lineas, existencias_actualizadas | Cierre de vale | Inventario, notificaciones, KPIs | A2/A3 |
| `se_cancelo_vale` | Vale anulado por autorización. | folio, motivo, aprobador | Cancelación de vale | Auditoría, reversión de existencias | A4 |
| `se_cerro_inventario` | Conteo físico finalizado. | tipo, responsable, diferencias, ajustes | Cierre de inventario | Ajustes, KPIs | A4 |
| `se_detecto_merma` | Producto dañado/caducado. | producto, cantidad, causa, foto, ubicacion | Detección de merma | Ajuste, calidad, notificaciones | A4 |
| `se_tomo_fotografia` | Usuario captura evidencia. | imagen, evento_asociado, usuario | Cualquier proceso con evidencia | Evidencias, auditoría | A2 |
| `se_recibio_oc` | Entrada completa/parcial de OC. | folio_oc, cantidad_recibida, faltantes, sobrantes | Recepción | Compras, contabilidad | A2 |
| `se_termino_surtido` | Picking de pedido completado. | pedido, productos, ubicaciones | Salida de mercancía | Logística, notificaciones | A2 |
| `se_imprimio_vale` | Vale exportado/impreso. | folio, usuario, formato | Cierre de vale | Auditoría | A0 |
| `stock_bajo_detectado` | Existencia ≤ punto de reorden. | producto, ubicacion, stock_actual, minimo | Scheduler o salida | Compras, inteligencia | A1 |
| `stock_negativo_detectado` | Validación detecta existencia negativa. | producto, ubicacion, cantidad | Validación de regla | Alerta, auditoría | A5 |
| `ubicacion_sobrecargada` | Rack excede capacidad. | rack, capacidad, ocupacion_actual | Validación de ubicación | Almacén, alertas | A1 |

### D3 — Compras

| Evento | Disparador | Payload | Generado por | Consumido por | Autonomía |
|--------|------------|---------|--------------|---------------|-----------|
| `se_creo_solicitud_compra` | Stock bajo o pedido de cliente. | producto, cantidad, solicitante, urgencia | Solicitud de compra | Compras | A1 |
| `se_creo_cotizacion` | Comprador solicita precio. | proveedores, producto, cantidad | Cotización | Comparación de proveedores | A0 |
| `se_creo_oc` | Selección de proveedor. | folio, proveedor, productos, total | Generación de OC | Aprobaciones, proveedor | A1/A3 |
| `se_envio_oc` | OC enviada al proveedor. | folio, proveedor, fecha_envio | Envío de OC | Seguimiento | A2 |
| `proveedor_retrasado` | OC no recibida en fecha. | folio_oc, dias_retraso | Seguimiento | Alertas, compras | A1 |
| `se_evaluo_proveedor` | Fin de período de evaluación. | proveedor, puntaje, metricas | Evaluación de proveedor | Inteligencia, compras | A0 |

### D5 — Logística

| Evento | Disparador | Payload | Generado por | Consumido por | Autonomía |
|--------|------------|---------|--------------|---------------|-----------|
| `pedido_listo_para_envio` | Surtido completado. | pedido, productos, peso, volumen | Salida de mercancía | Logística | A2 |
| `se_genero_ruta` | Agrupación de envíos. | ruta, envios, transportista | Planeación de rutas | Despacho | A2 |
| `se_genero_guia` | Transportista asignado. | envio, guia, transportista | Generación de guía | Cliente, seguimiento | A2 |
| `mercancia_despachada` | Camión sale del almacén. | envio, guia, transportista, foto | Despacho | Seguimiento | A2 |
| `entrega_confirmada` | Cliente recibe. | envio, cliente, fecha, firma/foto | Entrega | Facturación, KPIs | A2 |
| `entrega_fallida` | Cliente no recibe. | envio, causa, nueva_fecha | Entrega | Logística, ventas | A4 |
| `devolucion_iniciada` | Cliente devuelve mercancía. | pedido, productos, motivo | Devolución | Almacén, calidad | A4 |

### D2 — Ventas

| Evento | Disparador | Payload | Generado por | Consumido por | Autonomía |
|--------|------------|---------|--------------|---------------|-----------|
| `nuevo_lead` | Cliente potencial contacta. | canal, datos_contacto, necesidad | Captación de lead | CRM, ejecutivo | A1 |
| `cotizacion_creada` | Ejecutivo genera cotización. | cliente, productos, precios | Cotización | Seguimiento | A2 |
| `pedido_creado` | Cliente acepta cotización. | cliente, productos, total | Pedido | Almacén, reservas | A2 |
| `pedido_autorizado` | Pedido listo para surtir. | pedido, lineas | Autorización de pedido | Almacén | A3 |
| `descuento_solicitado` | Ejecutivo pide descuento fuera de política. | pedido, monto, motivo | Descuento | Aprobación | A4 |
| `pedido_facturado` | Pedido facturado. | pedido, factura | Facturación | Contabilidad | A2 |
| `queja_registrada` | Cliente reporta problema. | pedido, tipo, severidad | Postventa | Calidad, ventas | A4 |

### D6 — Calidad

| Evento | Disparador | Payload | Generado por | Consumido por | Autonomía |
|--------|------------|---------|--------------|---------------|-----------|
| `inspeccion_programada` | Programa de calidad lo indica. | lote, producto, fecha | Programación | Inspector | A1 |
| `lote_retenido` | Inspección no cumple estándar. | lote, producto, causa | Inspección | Almacén, compras | A4 |
| `lote_liberado` | Lote aprobado. | lote, producto | Inspección | Almacén | A3 |
| `no_conformidad_detectada` | Producto/proceso fuera de estándar. | tipo, producto, causa, evidencia | Detección | Acción correctiva | A4 |
| `accion_correctiva_creada` | NC requiere acción. | nc, responsable, fecha_limite | Análisis de causa | Seguimiento | A4 |
| `auditoria_realizada` | Fin de auditoría. | tipo, hallazgos, responsable | Auditoría | Acciones correctivas | A0 |

### D7 — Contabilidad

| Evento | Disparador | Payload | Generado por | Consumido por | Autonomía |
|--------|------------|---------|--------------|---------------|-----------|
| `factura_emitida` | Pedido facturado. | pedido, factura, cliente, total | Facturación | Cobranza | A2 |
| `pago_recibido` | Cliente paga. | factura, monto, fecha, metodo | Cobranza | Conciliación | A2 |
| `pago_programado` | Fecha de pago a proveedor. | oc, proveedor, monto, fecha | Cuentas por pagar | Aprobación | A1 |
| `pago_realizado` | Egreso confirmado. | pago, proveedor, monto | Pagos | Conciliación | A3/A4 |
| `nomina_generada` | Cálculo de nómina listo. | periodo, total, empleados | Nómina | Aprobación | A4 |

### D8 — RRHH

| Evento | Disparador | Payload | Generado por | Consumido por | Autonomía |
|--------|------------|---------|--------------|---------------|-----------|
| `empleado_contratado` | Alta de empleado. | nombre, puesto, fecha_ingreso | Alta | Expediente, asistencia | A2 |
| `asistencia_registrada` | Entrada/salida del día. | empleado, fecha, hora, tipo | Asistencia | Nómina | A2 |
| `permiso_solicitado` | Empleado pide permiso. | empleado, tipo, fechas | Permiso | Aprobación | A4 |
| `vacacion_aprobada` | Director autoriza vacaciones. | empleado, fechas | Vacaciones | Asistencia, planificación | A4 |
| `capacitacion_programada` | Plan anual de capacitación. | tema, fecha, participantes | Capacitación | Recordatorios | A1 |

### D9 — Inteligencia Empresarial

| Evento | Disparador | Payload | Generado por | Consumido por | Autonomía |
|--------|------------|---------|--------------|---------------|-----------|
| `reporte_solicitado` | Usuario pide reporte. | tipo, filtros, formato | Solicitud | Generador de reportes | A0/A2 |
| `kpi_actualizado` | Nuevo valor de indicador. | indicador, valor, meta, fecha | Cálculo de KPI | Dashboards, alertas | A0 |
| `alerta_generada` | KPI fuera de rango. | indicador, valor_actual, umbral | Monitoreo | Responsable | A1 |
| `inconsistencia_detectada` | Datos no coinciden. | entidad, campo, valores | Auditoría de datos | Responsable | A1 |
| `dashboard_publicado` | Dashboard actualizado. | nombre, fecha, destinatarios | Publicación | Dirección | A0 |

---

## 4. Eventos transversales

| Evento | Descripción | Disparador |
|--------|-------------|------------|
| `decision_tomada` | Se registró una decisión importante. | Cualquier decisión A4-A5. |
| `excepcion_detectada` | Ocurrió una situación fuera de regla. | Validación de reglas. |
| `error_de_sistema` | Falla técnica o de conector. | Monitoreo. |
| `modo_offline_activado` | CJ_OS opera sin conexión. | Falla de red. |

---

## 5. Criterios de aprobación

- [ ] Todos los eventos tienen nombre en formato `sustantivo_verbo`.
- [ ] Cada evento tiene disparador, payload, generador y consumidores.
- [ ] Los eventos críticos del dominio Almacén están completos.
- [ ] Carlos valida que los eventos reflejan la operación real.

---

## Historial de cambios

| Fecha | Versión | Cambio |
|-------|---------|--------|
| 2026-06-25 | 0.1.0 | Creación del Catálogo de Eventos con eventos iniciales por dominio. |
