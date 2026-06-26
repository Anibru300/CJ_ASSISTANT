# Análisis de BD_ALMACEN_3P

**Archivo analizado:** `G:\Mi unidad\zapia\Base de datos de almacen\BD_ALMACEN_3P_backup_20260625_173001.xlsx`  
**Copia de trabajo:** `workspace/almacen/data/BD_ALMACEN_3P_20260625.xlsx`  
**Fecha de análisis:** 2026-06-26  
**Analizó:** Kimi (Ingeniero DevOps)

---

## Resumen ejecutivo

Este archivo es el **sistema operativo real del almacén de 3P**. Contiene vales de salida, inventarios por almacén, catálogo de productos, resultados de inventario físico, auditoría y configuración. Es el insumo más valioso encontrado hasta ahora para validar el Modelo de Datos (M3) y preparar el KES-Pilot de entrada de mercancía.

**Conclusión:** Sí sirve, y mucho. Debe ser considerado fuente de verdad transitoria hasta migrar los datos a PostgreSQL.

---

## 1. Estructura general del archivo

El archivo tiene **43 hojas**, agrupadas así:

| Grupo de hojas | Cantidad | Ejemplos | Propósito |
|---|---|---|---|
| **Tablas maestras** | 9 | `VALES`, `DETALLE_VALES`, `ENTREGADO_A`, `PEDIDO_VALE_ASIGNACION`, `PEDIDOS_FACTURAS`, `DETALLE_PEDIDOS`, `FOTOS_PRODUCTOS`, `RESULTADOS_INVENTARIO`, `MINI_SAE` | Control de movimientos, pedidos, inventarios y catálogo. |
| **Inventarios por almacén** | 24 | `1 A-1 ROXELL`, `2 A-2 LUBING`, `40 A-40 FANCOM`, `99 Almacén 99`, `100 A-100 AJUSTE INVENTARIO` | Cada hoja representa una **ubicación/almacén lógico** con su propio inventario. |
| **Operativas** | 4 | `PRESTAMOS`, `PRUEBAS`, `MUESTRAS`, `CONFIG_BD` | Registros especiales de movimientos y configuración. |
| **Auditoría/Logs** | 4 | `CONFIG`, `LOG_AUDITORIA`, `HISTORIAL_AJUSTES`, `LOG_DASHBOARD` | Control de cambios, ajustes y eventos del sistema. |

---

## 2. Hallazgos clave

### 2.1 Vales de salida (hoja `VALES`)

- **226 vales** registrados desde septiembre de 2025.
- Los tipos de salida reales son:
  - `VENTA` (73)
  - `CONSIGNA` (57)
  - `PRUEBA` (34)
  - `COMODATO` (21)
  - `PRESTAMO` (18)
  - `PENDIENTE` (16)
  - `MUESTRA` (3)
  - `HERRAMIENTA` (1)
- Hay **138 vales cerrados** y **87 abiertos**.
- Quienes capturan: Francisco, Carlos, Christian, Salvador.
- Quienes entregan: Francisco Morales, Christian Contreras, Carlos Urbina, Salvador Morales.

**Implicación para el modelo de datos:**  
El campo `vales.tipo` propuesto en M3 debe separarse en:
- `tipo`: `salida` (porque todos estos son salidas del almacén).
- `motivo` o `subtipo`: `VENTA`, `CONSIGNA`, `PRUEBA`, `COMODATO`, `PRESTAMO`, `MUESTRA`, `HERRAMIENTA`, `PENDIENTE`.

### 2.2 Detalle de vales (hoja `DETALLE_VALES`)

- **925 líneas** de movimiento.
- **425 códigos de producto distintos**.
- Campos importantes:
  - `FOLIO_VALE` (relación con VALES).
  - `CANTIDAD`, `CODIGO`, `DESCRIPCION`.
  - `PEDIMENTO`, `NO_SERIE`.
  - `PEDIDO_INTERNO`, `NO_FACTURA`.
  - `ALMACEN_ORIGEN` (actualmente siempre `ALMACEN LEON`).
  - `CANTIDAD_VIVA` (270 líneas con cantidad viva > 0).
  - `CANT_ASIGNADA_PEDIDO`, `AJUSTE_MANUAL`, `CANT_AJUSTADA`.

**Implicación:** El modelo debe soportar:
- Números de serie y pedimentos por línea.
- Asignación parcial de líneas a pedidos.
- Ajustes manuales con auditoría (`HISTORIAL_AJUSTES`).

### 2.3 Almacenes / ubicaciones

Hay **24 hojas de almacén**. Cada una representa un inventario separado:

- Almacenes de proveedor/cliente: `A-1 ROXELL`, `A-2 LUBING`, `A-10 GEORGIA POULTRY`, `A-11 CHORETIME`, etc.
- Almacenes especiales:
  - `A-4 MUESTRAS`
  - `A-30 SIN MOVIMIENTO`
  - `A-43 GARANTIAS`
  - `A-100 AJUSTE INVENTARIO`
  - `A-102 COMODATO TECNICOS LEO`
  - `A-CONSIGNA TECNICOS LEON`
  - `CONSIGNACION GPORRES`
  - `OPERACIONES INTERNACIONALES`
  - `HUIXCOPAC/MARTINEZ PRODUCT. DE VEGETALES`
  - `Almacén 99`

Cada hoja tiene las columnas:
- `CODIGO`, `DESCRIPCION`
- `Exist. almacen` (físico en esa ubicación)
- `Exist. inventario` (valor contable/inventariado)
- `Costo promedio`, `Ultimo costo`, `Valor de inventario`

**Implicación:** El modelo debe considerar que una **ubicación puede ser propiedad de un tercero** (consignación, comodato) o ser un almacén lógico especial (garantías, muestras, ajustes).

### 2.4 Mini SAE (hoja `MINI_SAE`)

- **3,029 productos** con información de SAE.
- Columnas:
  - `CODIGO`, `DESCRIPCION`
  - `TIPO DE COSTEO` (PEPS, Promedio, UEPS)
  - `EXISTENCIAS`
  - `CLAVE SAT`
  - `COSTO PROMEDIO`, `ULTIMO COSTO`
  - `FECHA DE ULTIMA COMPRA`, `FECHA DE ULTIMA VENTA`
  - `PENDIENTES POR RECIBIR`
  - `CON PEDIMENTO`, `CON SERIE`
  - `CLAVE ALTERNA`

**Implicación:** El catálogo de productos debe poder sincronizarse con SAE. Hay productos con serie, con pedimento, y con clave SAT.

### 2.5 Resultados de inventario físico

- **133 registros** de conteos.
- Campos: `FOLIO`, `FECHA_HORA`, `ALMACEN`, `CODIGO`, `DESCRIPCION`, `EXIST_SAE`, `VALES`, `PEDIDOS_SF`, `CONTEO_FISICO`, `DIFERENCIA`, `ESTADO`.
- Estados: `OK` (130), `DIF` (3).

**Implicación:** El modelo debe soportar **conteos cíclicos** y reconciliación entre existencia de SAE, vales y pedidos vs. conteo físico.

### 2.6 Configuración y auditoría

- `CONFIG_BD` guarda:
  - `FOLIO_SALIDA` = 100 (último folio de vale de salida).
  - `FOLIO_ENTRADA` = 100 (último folio de vale de entrada).
  - `VERSION` = 3.
  - `RUTA_BD`.
- `LOG_AUDITORIA`: 65 registros de apertura y guardado de vales.
- `HISTORIAL_AJUSTES`: 228 ajustes manuales con usuario, folio, cantidad original y nueva.

**Implicación:** CJ_OS debe replicar esta trazabilidad con las tablas `eventos` y `audit_log`.

---

## 3. Implicaciones para el Modelo de Datos (M3)

El modelo propuesto en `docs/DATA_MODEL.md` cubre la mayoría de las entidades, pero debe ajustarse para reflejar la realidad de este archivo:

| Aspecto actual en Excel | Ajuste sugerido en M3 |
|---|---|
| Vales con tipo `VENTA`, `CONSIGNA`, `PRUEBA`, etc. | Campo `vales.motivo` además de `vales.tipo`. |
| 24 almacenes/ubicaciones, algunos de terceros. | Tabla `ubicaciones` con campo `propietario` y `tipo` (propio, consignación, comodato, garantías, etc.). |
| Existencia física vs. inventariado por ubicación. | Tabla `existencias` con `cantidad_fisica` y `cantidad_inventario`. |
| Productos con serie y pedimento. | Tabla `productos` con flags `requiere_serie`, `requiere_pedimento`, `clave_sat`. |
| Conteos de inventario físico. | Tabla `conteos_inventario` relacionada con `existencias`. |
| Ajustes manuales con auditoría. | Flujo de ajuste que genere `audit_log` y `eventos`. |
| Folios de entrada y salida controlados. | Tabla/configuración de folios por tipo de documento. |

---

## 4. Preguntas para Carlos y el experto de Almacén

1. ¿El archivo `BD_ALMACEN_3P.xlsm` es el archivo maestro que se actualiza diariamente?
2. ¿Quién y cuándo genera los backups? ¿Hay un macro que los crea automáticamente?
3. ¿Los almacenes `A-1 ROXELL`, `A-2 LUBING`, etc., representan **inventario en consignación** de esos proveedores?
4. ¿Qué significa exactamente `CANTIDAD_VIVA` en el detalle de vales?
5. ¿Cuál es la diferencia entre `Exist. almacen` y `Exist. inventario` en las hojas de almacén?
6. ¿Los vales `ABIERTOS` son vales que aún no se surten completamente?
7. ¿Qué proceso genera un vale de `ENTRADA`? ¿Está registrado en otra hoja o archivo?
8. ¿La hoja `PEDIDOS_FACTURAS` y `DETALLE_PEDIDOS` están en uso actualmente? (aparecen vacías en el backup).

---

## 5. Respuestas de Carlos (2026-06-26)

1. **¿Los almacenes A-1 ROXELL, A-2 LUBING son consignación?**  
   No. Son **sub-almacenes** que forman parte del inventario de 3P. El número (A-1, A-2) identifica el almacén y el nombre es el proveedor asociado. El `MINI_SAE` es el inventario general concentrado. Un mismo código puede existir en varios sub-almacenes; comparten sub-almacén cuando varios proveedores pueden surtirlo.

2. **¿Qué es `CANTIDAD_VIVA`?**  
   Es lo que queda vivo de un vale. Ejemplo: un vale salieron 10 piezas, pero se han ido facturando gradualmente. Si ya se facturaron 5, quedan 5 vivas. Esas 5 piezas siguen formando parte del inventario y se usan para el conteo físico.

3. **¿Diferencia entre `Exist. inventario` y `Exist. almacen`?**  
   - `Exist. inventario` = cantidad en ese sub-almacén.  
   - `Exist. almacen` = cantidad total en todos los sub-almacenes incluyendo ese.  
   Ejemplo: en ROXELL hay 5 piezas y en LUBING hay 5 del mismo código. En ROXELL, `Exist. inventario` = 5 y `Exist. almacen` = 10.

4. **¿Los vales abiertos aún no se surten?**  
   No. Al crearse el vale, el material ya se mandó y se surtió. Un vale abierto significa que aún tiene cantidad viva > 0. Cuando la cantidad viva llega a 0 (porque ya se facturó o vendió todo), el vale se cierra.

5. **¿Dónde se registran las entradas de mercancía?**  
   Logística las ingresa directamente al **ERP SAE**. CJ_OS no las captura manualmente; las obtendrá de SAE mediante integración.

6. **¿La hoja `PEDIDOS_FACTURAS` se usa?**  
   Es una nueva implementación. Aún no se ha usado.

---

## 6. Implicaciones corregidas para el Modelo de Datos

| Hallazgo | Ajuste en M3 |
|---|---|
| Los sub-almacenes son inventario propio de 3P. | `ubicaciones.propietario` = "3P" por defecto; `es_propiedad_de_tercero` = false. |
| `Exist. almacen` es la suma de todos los sub-almacenes. | No se guarda en cada registro; se calcula con `SUM(existencias.cantidad_fisica)` por producto. |
| `CANTIDAD_VIVA` controla la vida de un vale. | `vale_lineas.cantidad_viva` es el campo clave; cuando llega a 0, `vales.estado` = cerrado. |
| Las entradas se capturan en SAE. | CJ_OS leerá entradas desde SAE; no se construye captura manual de entradas en esta fase. |
| Pedidos/facturas aún no se usan. | Se mantienen en el modelo como tablas preparadas, pero no son prioritarias. |

---

## 7. Próximos pasos recomendados

1. **Ajustar el Modelo de Datos (M3)** con los hallazgos de este análisis.
2. **Ejecutar el KES-Pilot de entrada de mercancía** usando este archivo como base de preguntas.
3. **Diseñar el conector Excel de almacén** para leer/escribir en este archivo mientras dura la migración.
4. **Planear la migración inicial** de productos, ubicaciones y existencias desde `MINI_SAE` y las hojas de almacén.

---

*Análisis generado automáticamente por CJ_OS.*
