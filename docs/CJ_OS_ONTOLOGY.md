# Ontología Empresarial — CJ_OS

**Versión:** 0.2.0  
**Fecha:** 2026-06-26  
**Estado:** Borrador en revisión — M2.5 Ontología Empresarial  
**Propósito:** Definir qué existe en 3P, cómo se llama, qué significa, qué atributos tiene y qué restricciones tiene cada entidad. Fuente semántica para el Modelo de Datos (M3).

---

## 1. ¿Qué es una ontología empresarial?

Una ontología no es una base de datos. Es un documento que define:

- **Entidades:** ¿qué cosas existen en el negocio?
- **Atributos:** ¿qué características tienen?
- **Relaciones:** ¿cómo se conectan entre sí?
- **Restricciones:** ¿qué no puede ocurrir?
- **Significado:** ¿qué representa cada concepto para la empresa?

> **La Ontología Empresarial es el ADN del modelo de datos.** PostgreSQL solo lo materializa.

---

## 2. Principios de la ontología de 3P

1. **Una entidad, un nombre.** No usar sinónimos para el mismo concepto.
2. **Un atributo, un significado claro.** Cada campo debe saberse para qué sirve.
3. **Toda relación es explícita.** No asumir conexiones.
4. **Toda restricción es negociable o innegociable.** Se debe documentar quién puede autorizar una excepción.
5. **La ontología evoluciona.** Se actualiza en cada KES/SIC.

---

## 3. Entidades por dominio

### D4 — Almacén

#### Producto
- **Definición:** Bien físico que la empresa compra, almacena y vende o consume.
- **Atributos:**
  - `sku` (único, obligatorio)
  - `descripcion`
  - `proveedor_principal`
  - `costo`
  - `precio_venta`
  - `unidad_de_medida`
  - `peso`
  - `dimensiones`
  - `fotografia`
  - `manual`
  - `es_material_indirecto` (booleano)
  - `requiere_inspeccion_de_calidad` (booleano)
- **Restricciones:**
  - SKU único en toda la empresa.
  - Si `es_material_indirecto = true`, no se vende al cliente.

#### Rack / Ubicación
- **Definición:** Lugar físico dentro del almacén donde se guardan productos.
- **Atributos:**
  - `codigo` (único)
  - `pasillo`
  - `nivel`
  - `zona`
  - `tipo` (picking, reserva, mermas, cuarentena)
  - `capacidad_maxima`
  - `productos_permitidos` (familias compatibles)
- **Restricciones:**
  - No puede excederse la capacidad máxima.
  - Algunos productos no pueden compartir ubicación (incompatibilidades).

#### Existencia
- **Definición:** Cantidad de un producto en una ubicación específica.
- **Atributos:**
  - `producto`
  - `ubicacion`
  - `cantidad_fisica`
  - `cantidad_comprometida`
  - `cantidad_disponible`
  - `stock_minimo`
  - `stock_maximo`
  - `punto_reorden`
  - `ultimo_movimiento`
- **Restricciones:**
  - `cantidad_disponible = cantidad_fisica - cantidad_comprometida`.
  - `cantidad_fisica >= 0` siempre.
  - `cantidad_comprometida <= cantidad_fisica`.

#### Vale
- **Definición:** Documento que registra un movimiento de mercancía.
- **Atributos:**
  - `folio` (único)
  - `tipo` (entrada, salida, transferencia, ajuste, merma)
  - `estado` (abierto, cerrado, cancelado)
  - `fecha`
  - `responsable`
  - `motivo`
  - `lineas`
  - `evidencias`
- **Restricciones:**
  - Un vale cerrado no se modifica; se revierte.
  - Toda salida requiere responsable.

#### Orden de Compra (OC)
- **Definición:** Pedido formal a un proveedor para adquirir productos.
- **Atributos:**
  - `folio`
  - `proveedor`
  - `fecha_emision`
  - `estado` (abierta, parcial, cerrada, cancelada)
  - `lineas`
  - `total`
  - `moneda`
- **Restricciones:**
  - OC cancelada no puede recibirse.
  - OC mayor a umbral requiere aprobación.

#### Merma
- **Definición:** Producto que deja de ser útil por daño, caducidad o pérdida.
- **Atributos:**
  - `producto`
  - `cantidad`
  - `causa`
  - `evidencia_fotografica`
  - `responsable`
  - `aprobador`
  - `estado`
- **Restricciones:**
  - Toda merma requiere evidencia.
  - No puede aplicarse merma sin aprobación según nivel.

#### Pedido
- **Definición:** Solicitud de un cliente para adquirir productos.
- **Atributos:**
  - `folio`
  - `cliente`
  - `fecha`
  - `estado` (nuevo, reservado, surtido, enviado, facturado, cancelado)
  - `lineas`
  - `total`
  - `factura`
- **Restricciones:**
  - Pedido cancelado no genera salida.
  - Reserva solo si hay disponibilidad.

#### Inventario / Conteo
- **Definición:** Proceso de verificación física de existencias.
- **Atributos:**
  - `tipo` (ciclico, general)
  - `fecha`
  - `responsable`
  - `estado` (abierto, cerrado)
  - `diferencias`
  - `ajustes_generados`
- **Restricciones:**
  - Inventario cerrado no se reabre; se genera nuevo conteo si es necesario.

#### Material indirecto
- **Definición:** Producto no vendible que se consume en la operación.
- **Atributos:**
  - `sku`
  - `descripcion`
  - `familia`
  - `stock`
  - `ubicacion`
  - `responsable`
- **Restricciones:**
  - No aparece en facturas de venta.
  - Debe tener control de consumo.

#### Evidencia fotográfica
- **Definición:** Imagen vinculada a un evento o documento operativo.
- **Atributos:**
  - `imagen`
  - `fecha`
  - `usuario`
  - `evento_asociado`
  - `documento_vinculado`
- **Restricciones:**
  - Toda evidencia debe pertenecer a un evento o documento.

---

### D2 — Ventas

#### Cliente
- **Definición:** Persona o empresa que compra productos a 3P.
- **Atributos:**
  - `codigo` (único)
  - `razon_social`
  - `rfc`
  - `direccion_fiscal`
  - `direccion_entrega`
  - `contacto_principal`
  - `telefono`
  - `correo`
  - `tipo` (mayorista, minorista, distribuidor, interno)
  - `limite_credito`
  - `dias_credito`
  - `estado`
  - `Comentarios`
- **Restricciones:**
  - RFC único si está registrado.
  - Cliente con saldo vencido no recibe pedido sin autorización.

#### Cotización
- **Definición:** Propuesta de precios y condiciones enviada a un cliente.
- **Atributos:**
  - `folio`
  - `cliente`
  - `fecha_emision`
  - `vigencia_dias`
  - `lineas`
  - `subtotal`
  - `impuestos`
  - `Lab`
  - `Atencion a`
  - `total`
  - `estado` (borrador, enviada, aceptada, rechazada, vencida)
- **Restricciones:**
  - Cotización vencida no se convierte en pedido sin revisión.
  - Precios deben respetar listas autorizadas.

#### Factura
- **Definición:** Comprobante fiscal de venta emitido al cliente.
- **Atributos:**
  - `folio_fiscal`
  - `pedido`
  - `cliente`
  - `fecha_emision`
  - `subtotal`
  - `impuestos`
  - `total`
  - `estado` (activa, cancelada)
  - `xml`
  - `pdf`
- **Restricciones:**
  - Factura cancelada requiere motivo documentado.
  - No se factura sin pedido o vale asociado.

---

### D3 — Compras

#### Proveedor
- **Definición:** Persona o empresa que vende productos o servicios a 3P.
- **Atributos:**
  - `codigo` (único)
  - `razon_social`
  - `rfc`
  - `direccion`
  - `contacto_compras`
  - `telefono`
  - `correo`
  - `dias_entrega_estandar`
  - `moneda`
  - `estado` (activo, inactivo, bloqueado)
- **Restricciones:**
  - Proveedor bloqueado no recibe órdenes de compra.
  - RFC único.

#### Cotización de compra
- **Definición:** Precio y condiciones ofrecidos por un proveedor para un producto.
- **Atributos:**
  - `proveedor`
  - `producto`
  - `precio`
  - `moneda`
  - `vigencia`
  - `cantidad_minima`
  - `condiciones_entrega`
- **Restricciones:**
  - Cotización vencida no se usa para comparar.

---

### D5 — Logística

#### Transporte
- **Definición:** Medio o servicio utilizado para entregar mercancía al cliente.
- **Atributos:**
  - `codigo`
  - `tipo` (propio, tercero, paquetería, cliente recoge)
  - `nombre_operador`
  - `placa` (si aplica)
  - `telefono`
  - `capacidad`
- **Restricciones:**
  - Transporte de tercero debe tener guía o evidencia de entrega.

#### Guía
- **Definición:** Número de rastreo asociado a un envío.
- **Atributos:**
  - `numero`
  - `transporte`
  - `pedido`
  - `fecha_envio`
  - `fecha_entrega_estimada`
  - `url_rastreo`
  - `estado` (enviado, en_transito, entregado, fallido)
- **Restricciones:**
  - Guía entregada requiere confirmación o evidencia.

#### Entrega
- **Definición:** Confirmación de que el cliente recibió la mercancía.
- **Atributos:**
  - `pedido`
  - `guia`
  - `fecha_entrega`
  - `recibio`
  - `evidencia_fotografica`
  - `estado` (completa, parcial, rechazada)
- **Restricciones:**
  - Entrega rechazada genera incidente de logística.

---

### D6 — Calidad

#### Inspección
- **Definición:** Revisión de mercancía para verificar conformidad con especificaciones.
- **Atributos:**
  - `folio`
  - `tipo` (recepcion, en_proceso, salida)
  - `producto`
  - `cantidad_muestra`
  - `criterios`
  - `resultado` (aprobado, rechazado, condicional)
  - `inspector`
  - `fecha`
  - `evidencia`
- **Restricciones:**
  - Producto rechazado no pasa a inventario sin excepción documentada.

#### No conformidad
- **Definición:** Registro de un producto o proceso que no cumple con el estándar.
- **Atributos:**
  - `folio`
  - `tipo` (producto, proceso, documento)
  - `descripcion`
  - `severidad` (leve, mayor, crítica)
  - `area_responsable`
  - `estado` (abierta, en_analisis, cerrada)
  - `accion_correctiva`
- **Restricciones:**
  - No conformidad crítica detiene el proceso hasta resolución.

#### Acción correctiva
- **Definición:** Medida tomada para eliminar la causa de una no conformidad.
- **Atributos:**
  - `no_conformidad`
  - `descripcion`
  - `responsable`
  - `fecha_compromiso`
  - `fecha_cierre`
  - `evidencia`
  - `estado`
- **Restricciones:**
  - Acción correctiva vencida escala a Dirección.

---

### D7 — Contabilidad

#### Cuenta por cobrar
- **Definición:** Derecho de cobro a un cliente por venta realizada.
- **Atributos:**
  - `cliente`
  - `factura`
  - `monto`
  - `saldo`
  - `fecha_vencimiento`
  - `estado` (pendiente, parcial, pagada, vencida)
- **Restricciones:**
  - No se libera pedido si el cliente excede límite de crédito.

#### Cuenta por pagar
- **Definición:** Obligación de pago a un proveedor.
- **Atributos:**
  - `proveedor`
  - `factura`
  - `monto`
  - `saldo`
  - `fecha_vencimiento`
  - `estado`
- **Restricciones:**
  - Pago requiere autorización según monto.

---

### D8 — RRHH

#### Empleado
- **Definición:** Persona que labora en 3P.
- **Atributos:**
  - `numero_empleado` (único)
  - `nombre`
  - `puesto`
  - `departamento`
  - `fecha_ingreso`
  - `correo`
  - `telefono`
  - `estado` (activo, baja)
- **Restricciones:**
  - Empleado de baja no puede autorizar movimientos.

#### Puesto
- **Definición:** Rol organizacional con responsabilidades definidas.
- **Atributos:**
  - `codigo`
  - `nombre`
  - `departamento`
  - `nivel_autorizacion`
  - `permisos`
- **Restricciones:**
  - Un empleado solo puede tener un puesto principal activo.

---

### Entidades transversales

#### Usuario
- **Definición:** Persona con acceso al sistema CJ_OS.
- **Atributos:**
  - `username` (único)
  - `nombre`
  - `correo`
  - `rol`
  - `modulos_permitidos`
  - `nivel_autonomia`
  - `estado`
- **Restricciones:**
  - Usuario inactivo no puede iniciar sesión.
  - Las acciones quedan auditadas con este usuario.

#### Evento
- **Definición:** Cualquier ocurrencia relevante registrada por CJ_OS.
- **Atributos:**
  - `id`
  - `tipo` (sustantivo_verbo)
  - `timestamp`
  - `actor`
  - `entidad_afectada`
  - `payload`
  - `nivel` (info, advertencia, error, crítico)
- **Restricciones:**
  - Evento crítico siempre genera alerta.

#### Auditoría
- **Definición:** Registro inmutable de quién hizo qué, cuándo y por qué.
- **Atributos:**
  - `id`
  - `usuario`
  - `accion`
  - `entidad`
  - `valor_anterior`
  - `valor_nuevo`
  - `timestamp`
  - `motivo`
- **Restricciones:**
  - No se borran registros de auditoría.

---

## 4. Relaciones entre entidades (resumen)

```text
Producto ──se almacena en──────► Rack
Producto ──pertenece a─────────► Proveedor
Producto ──tiene───────────────► Existencia
Existencia ──se encuentra en───► Ubicacion
Vale ──consume/produce─────────► Producto
Inventario ──contiene──────────► Producto
Merma ──afecta─────────────────► Existencia
OC ──genera────────────────────► Entrada
Entrada ──actualiza────────────► Existencia
Pedido ──genera────────────────► Salida
Salida ──actualiza─────────────► Existencia
Transferencia ──mueve──────────► Existencia entre Ubicaciones
Evidencia ──pertenece a────────► Vale / Merma / Inventario / Entrega
Cliente ──hace─────────────────► Pedido
Pedido ──genera────────────────► Factura
Pedido ──se entrega mediante───► Guia
Guia ──pertenece a─────────────► Transporte
Proveedor ──recibe─────────────► OC
Proveedor ──emite──────────────► Factura (compra)
Producto ──se inspecciona en───► Inspeccion
Inspeccion ──puede generar─────► NoConformidad
NoConformidad ──requiere───────► AccionCorrectiva
Empleado ──tiene───────────────► Puesto
Usuario ──corresponde a────────► Empleado
Evento ──afecta a──────────────► Cualquier entidad
Auditoria ──registra cambios───► Cualquier entidad
```

---

## 5. Restricciones transversales

| Restricción | Tipo | Prioridad | ¿Se puede romper? | Evento relacionado |
|-------------|------|-----------|-------------------|--------------------|
| Existencia nunca negativa | Integridad | Alta | No | `ajuste_inventario` |
| Vale cerrado no se modifica | Integridad | Alta | No | `se_modifico_vale` |
| Toda merma requiere evidencia | Flujo | Alta | No | `se_detecto_merma` |
| Toda entrada requiere proveedor | Integridad | Media | Con autorización | `llego_mercancia` |
| Stock comprometido ≤ existencia física | Integridad | Alta | No | `se_creo_vale` |
| OC mayor a umbral requiere aprobación | Autorización | Alta | Solo por Director | `se_creo_oc` |
| Cliente con saldo vencido no recibe pedido | Autorización | Alta | Solo por Dirección | `se_creo_pedido` |
| Producto rechazado no entra a inventario | Calidad | Alta | Solo con excepción documentada | `inspeccion_rechazada` |
| No conformidad crítica detiene el proceso | Calidad | Alta | No | `no_conformidad_critica` |
| Acción correctiva vencida escala a Dirección | Calidad | Media | No | `accion_correctiva_vencida` |
| Factura cancelada requiere motivo | Integridad | Alta | No | `factura_cancelada` |
| Pago a proveedor requiere autorización según monto | Autorización | Alta | Solo por quien corresponda | `se_aprobo_pago` |
| Empleado de baja no autoriza movimientos | Seguridad | Alta | No | `intento_autorizacion_empleado_baja` |
| No se borran registros de auditoría | Seguridad | Alta | No | `intento_borrar_auditoria` |

---

## 6. Glosario de términos

| Término | Significado en 3P |
|---------|-------------------|
| **SKU** | Código único de producto. |
| **Rack** | Estante o ubicación física en almacén. |
| **Vale** | Documento de movimiento de mercancía. |
| **Existencia comprometida** | Stock reservado para pedidos ya autorizados. |
| **Merma** | Producto dañado, caducado o no conforme que sale del inventario. |
| **Conteo cíclico** | Inventario parcial y periódico de un grupo de productos. |
| **Material indirecto** | Insumos operativos no vendibles (cajas, cintas, herramientas). |
| **OC** | Orden de compra. |
| **No conformidad** | Producto o proceso que no cumple el estándar de calidad. |
| **Acción correctiva** | Medida para eliminar la causa de una no conformidad. |
| **Guía** | Número de rastreo de un envío. |
| **Cuenta por cobrar** | Derecho de cobro a cliente. |
| **Cuenta por pagar** | Obligación de pago a proveedor. |

---

## 7. Criterios de aprobación

- [x ] Cada entidad tiene nombre, definición, atributos y restricciones.
- [ x] No hay sinónimos para el mismo concepto.
- [ x] Las relaciones entre entidades son explícitas.
- [ x] Las restricciones indican si son negociables y quién autoriza excepciones.
- [ x] Carlos valida que la ontología representa la realidad de 3P.

---

## Historial de cambios

| Fecha | Versión | Cambio |
|-------|---------|--------|
| 2026-06-25 | 0.1.0 | Creación de la Ontología Empresarial con entidades iniciales de Almacén como patrón. |
| 2026-06-26 | 0.2.0 | Expansión de la ontología con entidades de Ventas, Compras, Logística, Calidad, Contabilidad, RRHH y transversales. Actualización de relaciones y restricciones. |
