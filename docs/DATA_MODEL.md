# Modelo de Datos — CJ_OS

**Versión:** 0.1.2  
**Fecha:** 2026-06-26  
**Estado:** Borrador ajustado con respuestas de Carlos sobre BD_ALMACEN_3P — M3 Modelo de Datos (pendiente de aprobación de Carlos)  
**Propósito:** Traducir la Ontología Empresarial de 3P a un esquema de PostgreSQL estructurado, trazable y escalable.

---

## 1. Principios del modelo de datos

1. **Una tabla por entidad principal** de la ontología.
2. **Toda acción importante se audita**: tabla `audit_log` registra cambios.
3. **Toda entidad tiene `id`, `created_at`, `updated_at` y `active`.**
4. **Las relaciones son explícitas** mediante claves foráneas.
5. **Los documentos y archivos no se guardan en la base de datos**; solo se guardan referencias y metadatos.
6. **El modelo soporta múltiples módulos de negocio** sin mezclar responsabilidades.
7. **Los nombres de tablas y columnas usan español** (según Business Dictionary de 3P).

---

## 2. Mapeo entidad → tabla

| Entidad (Ontología) | Tabla propuesta | Módulo |
|---------------------|-----------------|--------|
| Producto | `productos` | Almacén |
| Rack / Ubicación | `ubicaciones` | Almacén |
| Existencia | `existencias` | Almacén |
| Vale | `vales` / `vale_lineas` | Almacén |
| Motivo de salida | `motivos_salida` | Almacén |
| Orden de compra | `ordenes_compra` / `oc_lineas` | Compras |
| Merma | `mermas` | Almacén / Calidad |
| Conteo de inventario | `conteos_inventario` | Almacén |
| Folio / numeración | `folios` | Core |
| Pedido | `pedidos` / `pedido_lineas` | Ventas |
| Cliente | `clientes` | Ventas |
| Proveedor | `proveedores` | Compras |
| Cotización | `cotizaciones` / `cotizacion_lineas` | Ventas |
| Factura | `facturas` / `factura_lineas` | Ventas / Contabilidad |
| Transporte | `transportes` | Logística |
| Guía | `guias` | Logística |
| Entrega | `entregas` | Logística |
| Inspección | `inspecciones` | Calidad |
| No conformidad | `no_conformidades` | Calidad |
| Acción correctiva | `acciones_correctivas` | Calidad |
| Empleado | `empleados` | RRHH |
| Puesto | `puestos` | RRHH |
| Usuario | `usuarios` | Seguridad |
| Evento | `eventos` | Core |
| Auditoría | `audit_log` | Core |

---

## 3. Esquema de tablas propuesto (MVP)

### 3.1 Tablas transversales

```sql
-- Usuarios del sistema CJ_OS
CREATE TABLE usuarios (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    rol VARCHAR(50) NOT NULL,
    modulos_permitidos TEXT[],
    nivel_autonomia VARCHAR(20) DEFAULT 'A0',
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Empleados de 3P
CREATE TABLE empleados (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    numero_empleado VARCHAR(20) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    puesto_id UUID REFERENCES puestos(id),
    departamento VARCHAR(50),
    fecha_ingreso DATE,
    correo VARCHAR(100),
    telefono VARCHAR(20),
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Puestos organizacionales
CREATE TABLE puestos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    codigo VARCHAR(20) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    departamento VARCHAR(50),
    nivel_autorizacion VARCHAR(20),
    permisos TEXT[],
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### 3.2 Tablas de Ventas

```sql
-- Clientes
CREATE TABLE clientes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    codigo VARCHAR(20) UNIQUE NOT NULL,
    razon_social VARCHAR(200) NOT NULL,
    rfc VARCHAR(13) UNIQUE,
    direccion_fiscal TEXT,
    direccion_entrega TEXT,
    contacto_principal VARCHAR(100),
    telefono VARCHAR(20),
    correo VARCHAR(100),
    tipo VARCHAR(20) DEFAULT 'minorista',
    limite_credito DECIMAL(15,2),
    dias_credito INTEGER,
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Pedidos de clientes
CREATE TABLE pedidos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    folio VARCHAR(30) UNIQUE NOT NULL,
    cliente_id UUID REFERENCES clientes(id),
    fecha TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    estado VARCHAR(30) DEFAULT 'nuevo',
    subtotal DECIMAL(15,2),
    impuestos DECIMAL(15,2),
    total DECIMAL(15,2),
    responsable_id UUID REFERENCES empleados(id),
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Líneas de pedido
CREATE TABLE pedido_lineas (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pedido_id UUID REFERENCES pedidos(id) ON DELETE CASCADE,
    producto_id UUID REFERENCES productos(id),
    cantidad DECIMAL(12,3) NOT NULL,
    precio_unitario DECIMAL(15,2),
    total_linea DECIMAL(15,2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### 3.3 Tablas de Compras

```sql
-- Proveedores
CREATE TABLE proveedores (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    codigo VARCHAR(20) UNIQUE NOT NULL,
    razon_social VARCHAR(200) NOT NULL,
    rfc VARCHAR(13) UNIQUE,
    direccion TEXT,
    contacto_compras VARCHAR(100),
    telefono VARCHAR(20),
    correo VARCHAR(100),
    dias_entrega_estandar INTEGER,
    moneda VARCHAR(10) DEFAULT 'MXN',
    estado VARCHAR(20) DEFAULT 'activo',
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Órdenes de compra
CREATE TABLE ordenes_compra (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    folio VARCHAR(30) UNIQUE NOT NULL,
    proveedor_id UUID REFERENCES proveedores(id),
    fecha_emision DATE NOT NULL,
    estado VARCHAR(20) DEFAULT 'abierta',
    subtotal DECIMAL(15,2),
    impuestos DECIMAL(15,2),
    total DECIMAL(15,2),
    moneda VARCHAR(10) DEFAULT 'MXN',
    responsable_id UUID REFERENCES empleados(id),
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Líneas de OC
CREATE TABLE oc_lineas (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    orden_compra_id UUID REFERENCES ordenes_compra(id) ON DELETE CASCADE,
    producto_id UUID REFERENCES productos(id),
    cantidad DECIMAL(12,3) NOT NULL,
    precio_unitario DECIMAL(15,2),
    total_linea DECIMAL(15,2),
    cantidad_recibida DECIMAL(12,3) DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### 3.4 Tablas de Almacén

```sql
-- Productos
CREATE TABLE productos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    sku VARCHAR(50) UNIQUE NOT NULL,
    codigo_sae VARCHAR(50),
    descripcion VARCHAR(255) NOT NULL,
    familia VARCHAR(50),
    proveedor_principal_id UUID REFERENCES proveedores(id),
    clave_sat VARCHAR(20),
    costo DECIMAL(15,2),
    costo_promedio DECIMAL(15,2),
    ultimo_costo DECIMAL(15,2),
    precio_venta DECIMAL(15,2),
    unidad_de_medida VARCHAR(20),
    peso DECIMAL(10,3),
    dimensiones VARCHAR(50),
    fotografia_path TEXT,
    manual_path TEXT,
    es_material_indirecto BOOLEAN DEFAULT FALSE,
    requiere_inspeccion_calidad BOOLEAN DEFAULT FALSE,
    requiere_serie BOOLEAN DEFAULT FALSE,
    requiere_pedimento BOOLEAN DEFAULT FALSE,
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Ubicaciones / Racks / Almacenes logicos
CREATE TABLE ubicaciones (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    codigo VARCHAR(30) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    pasillo VARCHAR(10),
    nivel VARCHAR(10),
    zona VARCHAR(30),
    tipo VARCHAR(20), -- picking, reserva, mermas, cuarentena, consignacion, comodato, garantias
    propietario VARCHAR(100), -- 3P, ROXELL, LUBING, TECNICOS LEON, etc.
    es_propiedad_de_tercero BOOLEAN DEFAULT FALSE,
    capacidad_maxima DECIMAL(12,3),
    productos_permitidos TEXT[],
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Existencias
-- Nota: cantidad_fisica representa la existencia en ese sub-almacen/ubicacion.
-- El total general por producto (equivalente a MINI_SAE) se obtiene con SUM(cantidad_fisica).
CREATE TABLE existencias (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    producto_id UUID REFERENCES productos(id),
    ubicacion_id UUID REFERENCES ubicaciones(id),
    cantidad_fisica DECIMAL(12,3) DEFAULT 0,
    cantidad_comprometida DECIMAL(12,3) DEFAULT 0,
    cantidad_disponible DECIMAL(12,3) GENERATED ALWAYS AS (cantidad_fisica - cantidad_comprometida) STORED,
    stock_minimo DECIMAL(12,3),
    stock_maximo DECIMAL(12,3),
    punto_reorden DECIMAL(12,3),
    ultimo_movimiento TIMESTAMP WITH TIME ZONE,
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(producto_id, ubicacion_id)
);

-- Conteos de inventario fisico
CREATE TABLE conteos_inventario (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    folio VARCHAR(30) UNIQUE NOT NULL,
    fecha_hora TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    ubicacion_id UUID REFERENCES ubicaciones(id),
    producto_id UUID REFERENCES productos(id),
    existencia_sae DECIMAL(12,3) DEFAULT 0,
    existencia_vales DECIMAL(12,3) DEFAULT 0,
    existencia_pedidos DECIMAL(12,3) DEFAULT 0,
    conteo_fisico DECIMAL(12,3) NOT NULL,
    diferencia DECIMAL(12,3) GENERATED ALWAYS AS (conteo_fisico - existencia_sae) STORED,
    estado VARCHAR(10) DEFAULT 'OK', -- OK, DIF
    observaciones TEXT,
    responsable_id UUID REFERENCES empleados(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Control de folios por tipo de documento
CREATE TABLE folios (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tipo_documento VARCHAR(50) UNIQUE NOT NULL, -- vale_entrada, vale_salida, orden_compra, pedido, conteo
    prefijo VARCHAR(10),
    ultimo_folio INTEGER DEFAULT 0,
    longitud INTEGER DEFAULT 6,
    activo BOOLEAN DEFAULT TRUE,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Catálogo de motivos de salida (venta, consigna, prueba, comodato, prestamo, muestra, herramienta, etc.)
CREATE TABLE motivos_salida (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    codigo VARCHAR(30) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    requiere_devolucion BOOLEAN DEFAULT FALSE,
    es_transferencia_propiedad BOOLEAN DEFAULT TRUE,
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Vales de movimiento
CREATE TABLE vales (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    folio VARCHAR(30) UNIQUE NOT NULL,
    tipo VARCHAR(20) NOT NULL, -- entrada, salida, transferencia, ajuste, merma
    motivo_salida_id UUID REFERENCES motivos_salida(id),
    estado VARCHAR(20) DEFAULT 'abierto',
    fecha TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    responsable_id UUID REFERENCES empleados(id),
    entregado_a VARCHAR(200), -- persona o entidad destino
    observaciones TEXT,
    documento_origen_id UUID, -- puede referenciar OC, pedido, etc.
    documento_origen_tipo VARCHAR(50),
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Líneas de vale
CREATE TABLE vale_lineas (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    vale_id UUID REFERENCES vales(id) ON DELETE CASCADE,
    producto_id UUID REFERENCES productos(id),
    ubicacion_origen_id UUID REFERENCES ubicaciones(id),
    ubicacion_destino_id UUID REFERENCES ubicaciones(id),
    cantidad DECIMAL(12,3) NOT NULL,
    cantidad_viva DECIMAL(12,3) DEFAULT 0, -- cantidad pendiente de surtir/asignar
    cantidad_asignada_pedido DECIMAL(12,3) DEFAULT 0,
    costo_unitario DECIMAL(15,2),
    numero_serie VARCHAR(100),
    pedimento VARCHAR(100),
    pedido_interno VARCHAR(50),
    no_factura VARCHAR(50),
    comentarios TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### 3.5 Tablas de Core

```sql
-- Eventos del sistema
CREATE TABLE eventos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tipo VARCHAR(50) NOT NULL, -- sustantivo_verbo
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    actor_id UUID REFERENCES usuarios(id),
    actor_tipo VARCHAR(20), -- usuario, sistema, agente
    entidad_tipo VARCHAR(50),
    entidad_id UUID,
    payload JSONB,
    nivel VARCHAR(20) DEFAULT 'info',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Auditoría inmutable
CREATE TABLE audit_log (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    usuario_id UUID REFERENCES usuarios(id),
    accion VARCHAR(50) NOT NULL,
    entidad_tipo VARCHAR(50) NOT NULL,
    entidad_id UUID NOT NULL,
    valor_anterior JSONB,
    valor_nuevo JSONB,
    motivo TEXT,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

---

## 4. Índices propuestos

```sql
CREATE INDEX idx_productos_sku ON productos(sku);
CREATE INDEX idx_productos_codigo_sae ON productos(codigo_sae);
CREATE INDEX idx_productos_familia ON productos(familia);
CREATE INDEX idx_existencias_producto ON existencias(producto_id);
CREATE INDEX idx_existencias_ubicacion ON existencias(ubicacion_id);
CREATE INDEX idx_vales_folio ON vales(folio);
CREATE INDEX idx_vales_tipo ON vales(tipo);
CREATE INDEX idx_vales_motivo ON vales(motivo_salida_id);
CREATE INDEX idx_vale_lineas_serie ON vale_lineas(numero_serie);
CREATE INDEX idx_conteos_folio ON conteos_inventario(folio);
CREATE INDEX idx_conteos_ubicacion_producto ON conteos_inventario(ubicacion_id, producto_id);
CREATE INDEX idx_ordenes_compra_proveedor ON ordenes_compra(proveedor_id);
CREATE INDEX idx_pedidos_cliente ON pedidos(cliente_id);
CREATE INDEX idx_eventos_tipo ON eventos(tipo);
CREATE INDEX idx_eventos_entidad ON eventos(entidad_tipo, entidad_id);
CREATE INDEX idx_audit_entidad ON audit_log(entidad_tipo, entidad_id);
```

---

## 5. Restricciones de integridad clave

1. `existencias.cantidad_fisica >= 0`
2. `existencias.cantidad_comprometida <= existencias.cantidad_fisica`
3. `vales.estado` solo puede ser `abierto`, `cerrado`, `cancelado`.
4. `vale_lineas.cantidad > 0`
5. `productos.sku` único.
6. `clientes.rfc` único si no es nulo.
7. `proveedores.rfc` único si no es nulo.
8. Un vale de tipo `salida` debe tener un `motivo_salida_id`.
9. `ubicaciones.codigo` único.
10. `folios.tipo_documento` único.

---

## 6. Próximos pasos tras aprobación

1. Crear script SQL definitivo (`infrastructure/database/schema/001_initial_schema.sql`).
2. Ejecutar script en PostgreSQL de desarrollo.
3. Validar tablas, relaciones e índices.
4. Preparar respaldos automáticos.
5. Comenzar M4 — Integraciones con SAE y Excel de almacén.

---

## 7. Criterios de aprobación de M3

- [ ] El modelo cubre las entidades principales de la Ontología aprobada.
- [ ] Las relaciones reflejan procesos reales de 3P.
- [ ] Las restricciones protegen la integridad de datos.
- [ ] El modelo es escalable para nuevos módulos.
- [ ] Carlos aprueba el esquema propuesto.

---

## 8. Aprobación

| Rol | Nombre | Firma | Fecha |
|-----|--------|-------|-------|
| Product Owner / Director | Carlos | ____________________ | ________ |

**Comentarios:**

________________________________________________________________________

________________________________________________________________________

---

*Documento generado por Kimi el 2026-06-26 como borrador de M3 — Modelo de Datos.*
