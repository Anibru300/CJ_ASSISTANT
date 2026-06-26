# Validación de M3 — Modelo de Datos en PostgreSQL

**Fecha:** 2026-06-26  
**Base de datos:** `cj_os`  
**Servidor:** `cj_postgres` (PostgreSQL 16)  
**Script ejecutado:** `infrastructure/database/schema/001_initial_schema.sql`  
**Ejecutó:** Kimi (Ingeniero DevOps)

---

## Resumen

El Modelo de Datos M3 aprobado por Carlos fue traducido a un script SQL y ejecutado exitosamente en PostgreSQL. Se crearon 19 tablas con sus respectivos índices y 23 claves foráneas, sin errores.

---

## Tablas creadas

| # | Tabla | Descripción |
|---|-------|-------------|
| 1 | `usuarios` | Usuarios del sistema CJ_OS |
| 2 | `puestos` | Puestos organizacionales |
| 3 | `clientes` | Clientes de 3P |
| 4 | `proveedores` | Proveedores de 3P |
| 5 | `ubicaciones` | Sub-almacenes / ubicaciones |
| 6 | `folios` | Control de folios por documento |
| 7 | `motivos_salida` | Catálogo de motivos de salida |
| 8 | `eventos` | Eventos del sistema |
| 9 | `audit_log` | Auditoría inmutable |
| 10 | `empleados` | Empleados de 3P |
| 11 | `productos` | Catálogo de productos |
| 12 | `pedidos` | Pedidos de clientes |
| 13 | `ordenes_compra` | Órdenes de compra a proveedores |
| 14 | `vales` | Vales de movimiento |
| 15 | `existencias` | Existencias por producto y ubicación |
| 16 | `conteos_inventario` | Conteos físicos de inventario |
| 17 | `pedido_lineas` | Líneas de pedido |
| 18 | `oc_lineas` | Líneas de orden de compra |
| 19 | `vale_lineas` | Líneas de vale |

---

## Integridad referencial

Se crearon **23 claves foráneas**. Ejemplos:

- `empleados.puesto_id` → `puestos.id`
- `productos.proveedor_principal_id` → `proveedores.id`
- `pedidos.cliente_id` → `clientes.id`
- `ordenes_compra.proveedor_id` → `proveedores.id`
- `vales.motivo_salida_id` → `motivos_salida.id`
- `existencias.producto_id` → `productos.id`
- `existencias.ubicacion_id` → `ubicaciones.id`
- `vale_lineas.vale_id` → `vales.id`

---

## Índices creados

Se crearon **16 índices** para optimizar búsquedas frecuentes:

- `idx_productos_sku`, `idx_productos_codigo_sae`, `idx_productos_familia`
- `idx_existencias_producto`, `idx_existencias_ubicacion`
- `idx_vales_folio`, `idx_vales_tipo`, `idx_vales_motivo`
- `idx_vale_lineas_serie`
- `idx_conteos_folio`, `idx_conteos_ubicacion_producto`
- `idx_ordenes_compra_proveedor`, `idx_pedidos_cliente`
- `idx_eventos_tipo`, `idx_eventos_entidad`, `idx_audit_entidad`

---

## Comandos de validación

```bash
# Listar tablas
docker exec -i cj_postgres psql -U cj_user -d cj_os -c "\dt"

# Listar foreign keys
docker exec -i cj_postgres psql -U cj_user -d cj_os -c "
SELECT tc.table_name, kcu.column_name, ccu.table_name AS foreign_table, ccu.column_name AS foreign_column
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage ccu ON ccu.constraint_name = tc.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY'
ORDER BY tc.table_name;
"
```

---

## Estado

✅ **M3 — Modelo de Datos implementado y validado en PostgreSQL.**

---

*Reporte generado automáticamente por CJ_OS.*
