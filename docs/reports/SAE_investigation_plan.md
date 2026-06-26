# Investigación — Aspel-SAE 9.0 y conector seguro

**Fecha:** 2026-06-26  
**Objetivo:** Entender cómo Aspel-SAE 9.0 almacena la información antes de conectar CJ_OS.  
**Regla de oro:** Solo lectura. Nunca editar, eliminar ni mover archivos de SAE.  
**Responsable:** Kimi (Ingeniero DevOps)

---

## 1. Compromiso de seguridad con Carlos

Antes de cualquier acción sobre SAE, se aplica lo siguiente:

1. **No se tocará el archivo .fdb de producción.**
2. Se trabajará únicamente con **copias de respaldo** en un lugar seguro (`runtime/backups/sae_copy/`).
3. Cualquier conexión será de **solo lectura**.
4. Antes de copiar o consultar, se pedirá autorización explícita de Carlos.
5. No se ejecutarán comandos `INSERT`, `UPDATE`, `DELETE` ni `DROP` sobre la base de datos de SAE.
6. Si algo requiere cambio en SAE, se documentará y se hará manualmente por personal autorizado de 3P.

---

## 2. Hallazgos de investigación inicial

### 2.1 Motor de base de datos

- Aspel-SAE 9.0 usa **Firebird** como motor de base de datos.
- Toda la información se guarda en un solo archivo con extensión **.fdb**.
- Ruta típica: `C:\Program Files (x86)\Aspel\Aspel-SAE 9.0\Datos\SAE.fdb` o similar.

### 2.2 Estructura de tablas

Las tablas terminan con el número de empresa. Por ejemplo, para la empresa 1:

| Tabla | Descripción | Relevancia para CJ_OS |
|-------|-------------|-----------------------|
| `INVE01` | Catálogo de productos y existencias globales. | Alta — códigos, descripciones, existencias. |
| `FACT01` | Facturas de venta. | Alta — para cruzar con vales y cerrar cantidad viva. |
| `PEDIDO01` / `PEDIDOS01` | Pedidos de venta. | Alta — material que salió pero aún no se factura. |
| `CLIE01` | Catálogo de clientes. | Media — datos del cliente. |
| `PROV01` | Catálogo de proveedores. | Media — datos del proveedor. |
| `COMP01` | Compras / entradas de mercancía. | Media — entradas registradas por Logística. |
| `MULT01` | Multialmacén (existencias por almacén). | Alta — si usan varios almacenes en SAE. |
| `LTPD01` | Lotes y pedimentos. | Baja/Media — solo si aplica. |
| `DOCTOSIGF` | Enlace entre documentos de ventas (pedido → factura). | Alta — para seguir el flujo de documentos. |
| `DOCTOSIGC` | Enlace entre documentos de compras. | Media — para entradas. |
| `ALMACENES` | Catálogo de almacenes. | Media — nombres de almacenes. |
| `CFDI` | Información de timbrado CFDI. | Baja — para validación fiscal. |

> **Nota:** Los nombres exactos de tablas pueden variar ligeramente entre versiones de SAE. Se confirmarán al momento de la exploración.

### 2.3 Herramientas de conexión

Opciones para leer Firebird desde Python:

| Herramienta | Descripción | Estado |
|-------------|-------------|--------|
| `fdb` | Driver nativo de Python para Firebird. | Requiere instalación de librería cliente de Firebird. |
| `sqlalchemy-firebird` | Adaptador SQLAlchemy para Firebird. | Requiere `fdb` o `firebird-driver`. |
| `firebird-driver` | Driver moderno para Firebird 3+. | Alternativa a `fdb`. |
| `ISQL` (incluido con Aspel/ Firebird) | Consola de línea de comandos. | Ya disponible si Firebird está instalado. |
| `FlameRobin` / `IBExpert` | Herramientas gráficas. | Opcionales para exploración visual. |

### 2.4 Método seguro recomendado

1. **Copiar el .fdb** a `runtime/backups/sae_copy/SAE_YYYYMMDD_HHMMSS.fdb`.
2. **Conectar solo a la copia** usando `fdb` o `ISQL` en modo lectura.
3. **Listar tablas** con `SELECT RDB$RELATION_NAME FROM RDB$RELATIONS;`.
4. **Describir columnas** de tablas relevantes.
5. **Extraer muestras** pequeñas (top 5-10 registros) para validar estructura.
6. **Documentar** el mapa de tablas en `docs/reports/SAE_structure.md`.

---

## 3. Preguntas para Carlos

Para continuar de forma segura, necesito confirmar:

1. **¿Cuál es la ruta exacta del archivo .fdb de SAE?**
2. **¿Qué número de empresa usan?** (Ej. Empresa01, Empresa02)
3. **¿Cuál es el usuario y contraseña de Firebird?** (Por defecto suele ser `SYSDBA` / `masterkey`, pero Aspel a veces lo cambia.)
4. **¿Me autorizas a hacer una copia del .fdb en `runtime/backups/sae_copy/`?** La copia se hará con SAE cerrado o en horario de baja actividad para evitar corrupción.
5. **¿Hay algún horario en el que no se use SAE?** (Para hacer la copia sin riesgo.)

---

## 4. Próximos pasos

1. Esperar autorización de Carlos.
2. Realizar copia de seguridad del .fdb.
3. Instalar driver de Firebird en entorno aislado.
4. Explorar estructura de tablas.
5. Crear `docs/reports/SAE_structure.md`.
6. Diseñar conector de solo lectura para facturas y pedidos.

---

*Documento generado por CJ_OS.*
