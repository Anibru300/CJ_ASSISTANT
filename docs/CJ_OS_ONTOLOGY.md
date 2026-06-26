# Ontología Empresarial — CJ_OS

**Versión:** 0.1.0  
**Fecha:** 2026-06-25  
**Estado:** Borrador inicial — pendiente de M2.8 BKA  
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
  - `familia`
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

## 4. Relaciones entre entidades (resumen)

```text
Producto ──se almacena en──► Rack
Producto ──pertenece a────► Proveedor
Producto ──tiene──────────► Existencia
Existencia ──se encuentra en──► Ubicacion
Vale ──consume/produce────► Producto
Inventario ──contiene─────► Producto
Merma ──afecta────────────► Existencia
OC ──genera───────────────► Entrada
Entrada ──actualiza───────► Existencia
Pedido ──genera───────────► Salida
Salida ──actualiza────────► Existencia
Transferencia ──mueve─────► Existencia entre Ubicaciones
Evidencia ──pertenece a───► Vale / Merma / Inventario
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

---

## 7. Criterios de aprobación

- [ ] Cada entidad tiene nombre, definición, atributos y restricciones.
- [ ] No hay sinónimos para el mismo concepto.
- [ ] Las relaciones entre entidades son explícitas.
- [ ] Las restricciones indican si son negociables y quién autoriza excepciones.
- [ ] Carlos valida que la ontología representa la realidad de 3P.

---

## Historial de cambios

| Fecha | Versión | Cambio |
|-------|---------|--------|
| 2026-06-25 | 0.1.0 | Creación de la Ontología Empresarial con entidades iniciales de Almacén como patrón. |
