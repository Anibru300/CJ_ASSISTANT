# Changelog - CJ_Assistant

## Versión 0.0.30

**Fecha:** 2026-06-26

### Cambios realizados

- **Ejecución de la KES-Pilot de entrada de mercancía**:
  - Carlos respondió las 20 preguntas del cuestionario.
  - Se registraron las respuestas en `docs/reports/KES-Pilot_entrada_mercancia.md`.
  - Se creó `docs/reports/KES-Pilot_entrada_mercancia_synthesis.md` con la síntesis del proceso real.
- **Hallazgos principales validados**:
  - Logística y Compras es el mismo puesto en 3P.
  - Almacén recibe físicamente, cuenta e inspecciona; Logística registra la entrada en SAE.
  - SAE actualiza existencias automáticamente.
  - Sub-almacenes se asignan por proveedor.
  - Se toman fotos en cada recepción.
  - Excepciones más frecuentes: faltante y sobrante.
  - Productos líquidos (detergentes) y frágiles requieren inspección especial.
  - Excel y SAE no siempre coinciden; se corrigen con ajustes manuales.
- **Actualización del Business Dictionary**:
  - Se agregaron términos validados: Sub-almacén, Cantidad viva, Logística y Compras, Recepción, Cuarentena, Mini-SAE.
  - Versión actualizada a 0.3.0.
- **Actualización de la Knowledge Coverage Matrix**:
  - KES-Pilot marcada como completada.
  - Cobertura de Almacén elevada a "Avanzado" 🟢.
- **Actualización de `PENDIENTES.md`**:
  - KES-Pilot marcada como completada.
  - Foco actual: integraciones SAE/Excel y owner user en n8n.
- **No se crearon tablas adicionales.**
- **No se programó código de lógica de negocio real.**

## Versión 0.0.29

**Fecha:** 2026-06-26

### Cambios realizados

- **Inicio del KES-Pilot de entrada de mercancía**:
  - Se actualizó `docs/reports/KES-Pilot_entrada_mercancia.md` al enfoque real de 3P:
    - Entrada registrada por Logística en **Aspel-SAE**.
    - Distribución y control de existencias en **sub-almacenes** (A-1 ROXELL, A-2 LUBING, etc.).
    - Reflejo en inventario general (**Mini-SAE**).
  - Se agregó un **cuestionario práctico de 20 preguntas** para Carlos, Salvador o Francisco.
  - Se incluyeron eventos adicionales: `se_registro_entrada_en_sae`, `se_asigno_subalmacen`.
  - Se agregaron reglas R6 y R7 sobre asignación a sub-almacenes y conciliación con Mini-SAE.
- **Actualización de `PENDIENTES.md`**:
  - KES-Pilot marcado como en curso y foco principal.
- **No se programó código de lógica de negocio real.**

## Versión 0.0.28

**Fecha:** 2026-06-26

### Cambios realizados

- **Aprobación de M3 — Modelo de Datos por Carlos**:
  - Carlos aprobó `docs/DATA_MODEL.md` v0.1.2 el 26/06/2026.
  - Se creó `docs/reports/M3_approval_request.md` como registro formal de aprobación.
  - `docs/PROJECT_BIBLE.md`: M3 marcado como ✅ Completado y aprobado por Carlos.
  - `docs/ROADMAP.md`: M3 marcado como ✅ Completado y aprobado por Carlos.
- **Generación e implementación del esquema de PostgreSQL**:
  - Se generó `infrastructure/database/schema/001_initial_schema.sql` a partir de `docs/DATA_MODEL.md`.
  - Se ordenaron las tablas por dependencias para evitar errores de claves foráneas.
  - Se creó la base de datos `cj_os` en el servidor PostgreSQL.
  - Se ejecutó el script y se crearon **19 tablas**, **23 claves foráneas** y **16 índices** sin errores.
  - Se creó `docs/reports/M3_database_validation.md` con evidencia de validación.
- **Actualización de `PENDIENTES.md`**:
  - M3 marcado como implementado y validado.
  - Foco actual reordenado: M4 — Integraciones, owner user en n8n y KES-Pilot.
- **No se programó código de lógica de negocio real.**

## Versión 0.0.27

**Fecha:** 2026-06-26

### Cambios realizados

- **Incorporación de respuestas de Carlos sobre BD_ALMACEN_3P**:
  - Los sub-almacenes (A-1 ROXELL, A-2 LUBING, etc.) son inventario propio de 3P, clasificados por proveedor.
  - `MINI_SAE` es el inventario general concentrado.
  - `CANTIDAD_VIVA` es lo que queda por facturar/vender de un vale; mientras sea > 0, el vale está abierto.
  - `Exist. inventario` = existencia en ese sub-almacén; `Exist. almacen` = total en todos los sub-almacenes.
  - Las entradas de mercancía se capturan en SAE; CJ_OS las obtendrá por integración.
  - `PEDIDOS_FACTURAS` es una implementación nueva aún no usada.
- **Ajustes al Modelo de Datos (M3)**:
  - Se actualizó `docs/DATA_MODEL.md` a v0.1.2.
  - Se eliminó el campo `cantidad_inventario` de `existencias`; el total general se calculará con `SUM(cantidad_fisica)` por producto.
  - Se agregaron notas explicativas en la tabla `existencias`.
- **Actualización de reporte**:
  - `docs/reports/BD_ALMACEN_3P_analysis.md` ahora incluye la sección "Respuestas de Carlos" e implicaciones corregidas.
- **Actualización de `PENDIENTES.md`**:
  - M3 v0.1.2 listo para aprobación.
- **No se crearon tablas de PostgreSQL productivas** (rehén: aprobación de M3).
- **No se programó código de lógica de negocio real.**

## Versión 0.0.26

**Fecha:** 2026-06-26

### Cambios realizados

- **Análisis de la base de datos real de almacén**:
  - Se revisó `G:\Mi unidad\zapia\Base de datos de almacen\BD_ALMACEN_3P_backup_20260625_173001.xlsx`.
  - Se copió una versión de trabajo a `workspace/almacen/data/BD_ALMACEN_3P_20260625.xlsx` (solo lectura).
  - Se identificó que el archivo contiene 43 hojas: vales, detalle de vales, 24 inventarios por almacén, mini-SAE, resultados de inventario, fotos, configuración y auditoría.
  - Se creó `docs/reports/BD_ALMACEN_3P_analysis.md` con hallazgos clave y preguntas para el experto de almacén.
- **Ajustes al Modelo de Datos (M3)**:
  - Se actualizó `docs/DATA_MODEL.md` a v0.1.1 incorporando:
    - Tabla `motivos_salida` y campo `motivo_salida_id` en `vales`.
    - Campos `cantidad_viva`, `cantidad_asignada_pedido`, `numero_serie`, `pedimento`, `pedido_interno`, `no_factura` en `vale_lineas`.
    - Campos `propietario` y `es_propiedad_de_tercero` en `ubicaciones`.
    - Campos `codigo_sae`, `costo_promedio`, `ultimo_costo`, `clave_sat`, `requiere_serie`, `requiere_pedimento` en `productos`.
    - Campo `cantidad_inventario` en `existencias`.
    - Nuevas tablas: `conteos_inventario` y `folios`.
  - Se actualizaron índices y restricciones.
- **Actualización de `PENDIENTES.md`**:
  - M3 marcado como ajustado con hallazgos de BD_ALMACEN_3P.
- **No se crearon tablas de PostgreSQL productivas** (rehén: aprobación de M3).
- **No se programó código de lógica de negocio real.**

## Versión 0.0.25

**Fecha:** 2026-06-26

### Cambios realizados

- **Ejecución exitosa del Hello World end-to-end**:
  - Se inició el Core `core/api/hello_world.py` y respondió correctamente a `curl http://localhost:8000/hello`.
  - Se ejecutó el workflow `CJ_OS Hello World` por CLI de n8n:
    ```bash
    docker compose -f infrastructure/compose/docker-compose.yml --env-file .env run --rm --entrypoint n8n n8n execute --id=b2357379-f7b2-4266-a8f9-f1a64840c944
    ```
  - El workflow finalizó con estado `success` y el nodo HTTP Request recibió la respuesta esperada del Core.
  - Se creó `docs/reports/Hello_World_execution.md` con la evidencia de ejecución.
- **Actualización de documentación**:
  - `docs/HELLO_WORLD.md`: estado actualizado a "ejecutado por CLI"; pendiente owner user para GUI.
  - `PENDIENTES.md`: Hello World marcado como validado; foco actual reordenado hacia M3, owner user y KES-Pilot.
- **Preparación de M3 para aprobación**:
  - `docs/DATA_MODEL.md` v0.1.0 listo para revisión y aprobación de Carlos.
- **No se creó el owner user en n8n** (aún requiere GUI).
- **No se crearon tablas de PostgreSQL productivas** (rehén: aprobación de M3).
- **No se programó código de lógica de negocio real.**

## Versión 0.0.24

**Fecha:** 2026-06-26

### Cambios realizados

- **Aprobación de M2.5 — Ontología Empresarial por Carlos**:
  - Carlos revisó y aprobó `docs/CJ_OS_ONTOLOGY.md` v0.2.0 el 26/06/2026.
  - Se creó `docs/reports/M2.5_approval_request.md` como registro formal de aprobación.
  - `docs/PROJECT_BIBLE.md`: M2.5 marcado como ✅ Completado y aprobado por Carlos.
  - `docs/ROADMAP.md`: M2.5 marcado como ✅ Completado y aprobado por Carlos.
- **Actualización de `PENDIENTES.md`**:
  - M2.5 marcado como aprobado.
  - Foco actual reordenado: crear owner user en n8n, ejecutar KES-Pilot y avanzar a M3.
- **No se ejecutó el workflow en n8n** (rehén: falta crear owner user).
- **No se crearon tablas de PostgreSQL productivas** (rehén: aprobación de M3).
- **No se programó código de lógica de negocio real.**

## Versión 0.0.23

**Fecha:** 2026-06-26

### Cambios realizados

- **Configuración de API key en n8n**:
  - Se agregó `N8N_API_KEY` a `.env` y `.env.example`.
  - Se actualizó `infrastructure/compose/docker-compose.yml` para inyectar `N8N_API_KEY` en el contenedor `cj_n8n`.
  - n8n fue reiniciado y valida correctamente la variable (HTTP 200 en `http://localhost:5678`).
- **Importación automática del workflow Hello World**:
  - Se actualizó `infrastructure/n8n/workflows/hello_world.json` para incluir `id` y poder importarse por CLI.
  - Se importó el workflow en n8n mediante:
    ```bash
    docker compose -f infrastructure/compose/docker-compose.yml --env-file .env exec n8n n8n import:workflow --input=/tmp/hello_world.json
    ```
  - Listado de workflows confirma: `b2357379-f7b2-4266-a8f9-f1a64840c944 | CJ_OS Hello World`.
- **Preparación de KES-Pilot — Entrada de mercancía**:
  - Se creó `docs/reports/KES-Pilot_entrada_mercancia.md` con plan, preguntas, decisiones y entregables para la primera sesión de adquisición de conocimiento con el experto de Almacén.
- **Preparación de M3 — Modelo de Datos**:
  - Se creó `docs/DATA_MODEL.md` (borrador v0.1.0) con capa de negocio, lógica y física basado en la Ontología M2.5.
- **Actualización de documentación operativa**:
  - `docs/HELLO_WORLD.md`: se documentó la importación por CLI, la necesidad de un owner user para ejecutar workflows, y el estado actual.
  - `PENDIENTES.md`: se actualizó el foco actual a Ontología M2.5, owner user en n8n, KES-Pilot y M3.
- **No se ejecutó el workflow en n8n** (rehén: falta crear owner user).
- **No se crearon tablas de PostgreSQL productivas** (rehén: aprobación de M2.5 y M3).
- **No se programó código de lógica de negocio real.**

## Versión 0.0.22

**Fecha:** 2026-06-26

### Cambios realizados

- **Reinicio de Docker Desktop y servicios**:
  - Docker Desktop se inició correctamente.
  - Se aplicó la versión fija de n8n: `n8nio/n8n:2.27.4` (la base de datos ya había sido migrada con esta versión; se actualizó `docker-compose.yml` y se agregó nota explicativa).
  - Todos los contenedores (`cj_postgres`, `cj_redis`, `cj_n8n`) están healthy.
  - n8n responde correctamente en `http://localhost:5678`.
- **Auditoría de seguridad de `.env`**:
  - Se creó `testing/audit_env.py` para verificar si `.env` contiene credenciales reales.
  - Resultado: no se detectaron credenciales de producción; todos los valores sensibles son placeholders o rutas a archivos de configuración.
- **Preparación de Ontología Empresarial (M2.5)**:
  - Actualización de `docs/CJ_OS_ONTOLOGY.md` a versión 0.2.0.
  - Agregadas entidades de Ventas, Compras, Logística, Calidad, Contabilidad, RRHH y transversales.
  - Actualizadas relaciones, restricciones transversales y glosario.
- **Actualización de documentación**:
  - `docs/HELLO_WORLD.md`: se documentó que la importación del workflow en n8n requiere GUI o API key.
  - `PENDIENTES.md`: M2.5 como foco actual; Hello World con n8n parcialmente pendiente.
- **No se crearon tablas de PostgreSQL.**
- **No se programó código de lógica de negocio nueva.**

## Versión 0.0.21

**Fecha:** 2026-06-26

### Cambios realizados

- **Aprobación de M2.4 por Carlos**:
  - `docs/reports/M2.4_approval_request.md` firmado/aprobado por Carlos el 26/06/2026.
  - `docs/PROJECT_BIBLE.md`: M2.4 marcado como ✅ Completado.
  - `docs/ROADMAP.md`: M2.4 marcado como ✅ Completado.
- **Aplicación de decisiones de Carlos**:
  - Eliminación de `docs/archive/CORE_ARCHITECTURE.md` (decisión de Carlos).
  - Confirmación del término oficial "módulos" para las áreas de negocio.
  - Variables de IA dejadas como pendiente hasta decidir proveedor.
- **Nuevo foco del proyecto**: Milestone M2.5 — Ontología Empresarial.
- **Actualización de `PENDIENTES.md`**: M2.4 cerrado; M2.5 como foco actual.
- **Creación de `docs/reports/CJ_OS_CONTROL_AND_IMPROVEMENTS.md`**: recomendaciones de control, seguridad, monitoreo, calidad del conocimiento y plan de acción priorizado, solicitadas por Carlos.
- **No se programó código nuevo.**
- **No se crearon tablas de PostgreSQL.**
- **No se modificó la base de datos.**

## Versión 0.0.20

**Fecha:** 2026-06-26

### Cambios realizados

- **Preparación del paquete de aprobación de M2.4**:
  - Creación de `docs/reports/M2.4_approval_request.md` con resumen ejecutivo, documentos incluidos, inconsistencias corregidas, pendientes por decidir, criterios de aprobación y espacio para firma de Carlos.
  - Actualización de `PENDIENTES.md` para indicar que el paquete está listo para revisión de Carlos.
- **No se programó código nuevo.**
- **No se crearon tablas de PostgreSQL.**
- **No se modificó la base de datos.**

## Versión 0.0.19

**Fecha:** 2026-06-26

### Cambios realizados

- **Creación del Hello World end-to-end** para validar comunicación entre n8n y el Core:
  - `core/api/hello_world.py`: servidor HTTP minimalista usando solo librería estándar de Python.
  - `core/hello_world_cli.py`: versión por línea de comandos invocable desde n8n.
  - `testing/test_hello_world.py`: pruebas automáticas del CLI y del módulo HTTP.
  - `infrastructure/n8n/workflows/hello_world.json`: workflow exportable para n8n.
  - `docs/HELLO_WORLD.md`: guía de uso e importación en n8n.
- **Preparación del proyecto para código Python**:
  - Creación de `core/__init__.py`, `core/api/__init__.py` y `testing/__init__.py`.
  - Actualización de `core/api/README.md` y `core/README.md` para reflejar el estado actual.
- **No se crearon tablas de PostgreSQL.**
- **No se modificó la base de datos.**
- **La prueba con n8n queda pendiente** porque Docker no está activo en este momento.

## Versión 0.0.18

**Fecha:** 2026-06-26

### Cambios realizados

- **Cierre de inconsistencias documentales detectadas en M2.4**:
  - Actualización de `docs/ROADMAP.md` para reflejar que M2.4 es **Auditoría y Aprobación Documental** (no Ontología).
  - Reordenamiento de submilestones posteriores: M2.5 Ontología, M2.6 Eventos, M2.7 Decisiones, M2.8 Reglas, M2.9 BKA.
  - Actualización de `docs/PROJECT_BIBLE.md`: M2.4 en espera de aprobación de Carlos; agregado M2.5 Ontología Empresarial.
  - Actualización de `README.md`: estado actual con M1 completado y M2.4 en espera de aprobación.
  - Actualización de `PENDIENTES.md`: limpieza de disco marcada como completada; M2.4 como foco actual.
- **Verificación de `docs/CJ_OS_BLUEPRINT.md`**: ya refleja cinco niveles del Core (Memory, Knowledge, Rules, Goals, Behavior) y los 15 componentes del Core; no requirió ajustes.
- **Verificación de `docs/DECISIONS.md`**: ya registra decisiones de M2.2 (Arquitectura Cognitiva), M2.3 (Filosofía) y la reorganización de M2; no requirió ajustes mayores.
- **No se programó código.**
- **No se crearon tablas de PostgreSQL.**
- **No se modificó la base de datos.**
- **No se reinició n8n** (Docker no estaba disponible).

## Versión 0.0.17

**Fecha:** 2026-06-26

### Cambios realizados

- **Limpieza de estructura de carpetas**:
  - Eliminación de las carpetas numeradas vacías: `01_n8n/`, `04_google_drive/`, `05_onedrive/`, `06_sae/`, `07_excel_almacen/`, `08_whatsapp/`, `09_prompts/`, `10_pruebas/`.
  - Motivo: duplicaban la estructura organizada en `ai/`, `connectors/`, `modules/`, `workspace/` y `core/`, generando confusión.
  - Se mantienen `02_backups/` y `03_logs/` como directorios operativos locales.
- **Inicialización del repositorio Git y publicación en GitHub**:
  - Se inicializó el repositorio local en `C:\Projects\CJ_Assistant`.
  - Se configuró el remoto `origin` apuntando a `https://github.com/Anibru300/CJ_ASSISTANT`.
  - Se realizó el commit inicial con la estructura base, infraestructura y configuración segura.
  - Se verificó que `.env`, `runtime/`, `02_backups/` y `03_logs/` no se subieron al repositorio gracias a `.gitignore`.
- **Actualización de `PENDIENTES.md`**:
  - Se marcó como completada la limpieza de carpetas numeradas.
  - Se marcó como completada la publicación en GitHub.
  - Se mantuvieron los pendientes que requieren decisión de Carlos o disponibilidad de Docker.
- **No se programó código.**
- **No se crearon tablas de PostgreSQL.**
- **No se crearon APIs.**
- **No se tocó la base de datos.**
- **No se reinició n8n** (Docker no estaba disponible en el momento de la operación).

## Versión 0.0.16

**Fecha:** 2026-06-25

### Cambios realizados

- Inicio del Milestone **M2.4 — Auditoría y Aprobación Documental**, autorizado por Carlos.
- Revisión de los siguientes documentos sin modificarlos:
  - `docs/CJ_OS_BLUEPRINT.md`
  - `docs/CJ_OS_PHILOSOPHY.md`
  - `docs/CORE_ARCHITECTURE.md`
  - `docs/SYSTEM_MAP.md`
  - `docs/ROADMAP.md`
  - `docs/DECISIONS.md`
- Generación del reporte `docs/reports/M2.4_documentation_audit.md` con:
  - Matriz de evaluación por documento.
  - Identificación de documentos redundantes.
  - Identificación de contradicciones.
  - Identificación de partes demasiado abstractas.
  - Lista de documentos necesarios para M3.
  - Propuesta de paquete mínimo de documentos aprobables.
- Actualización de `docs/ROADMAP.md` para incluir M2.4.
- Actualización de `docs/PROJECT_BIBLE.md` para reflejar M2.4.
- Actualización de `docs/INSTALL_LOG.md`.
- **No se crearon documentos de arquitectura nuevos.**
- **No se agregaron nuevas ideas de diseño.**
- **No se crearon carpetas.**
- **No se programó código.**
- **No se modificaron los documentos originales.**
- Estado: en espera de aprobación de Carlos para continuar.

## Versión 0.0.15

**Fecha:** 2026-06-25

### Cambios realizados

- Aprobación del Milestone **M2.3 — Filosofía y Constitución de CJ_OS**, propuesto por Carlos.
- Creación del documento conceptual **`docs/CJ_OS_PHILOSOPHY.md`** — The Mind of CJ_OS.
- Definición de la **quinta capa del Core**: `core/behavior/`.
- Documentación de los cinco niveles del criterio de CJ_OS:
  - Memory — ¿Qué pasó?
  - Knowledge — ¿Cómo funciona?
  - Rules — ¿Qué está permitido?
  - Goals — ¿Qué se intenta lograr?
  - Behavior — ¿Cómo debe comportarse?
- Definición de la **misión** de CJ_OS: ser el empleado digital más confiable de 3P.
- Definición de **valores**: confianza, responsabilidad, servicio, precisión, mejora continua, seguridad, trazabilidad, humildad operativa.
- Definición del **comportamiento profesional**:
  - Cómo escribe (tono, formalidad, claridad, emojis).
  - Cómo toma decisiones (conservador, proactivo, escalamiento).
  - Cómo maneja errores (nunca inventa datos, pregunta, escala, audita).
  - Cómo prioriza (seguridad, datos, clientes, operación, velocidad).
  - Cómo aprende (propone, espera aprobación, documenta).
- Redacción de la **Constitución de CJ_OS** con 8 leyes fundamentales:
  1. Nunca perder información.
  2. Nunca modificar datos críticos sin autorización.
  3. Toda acción importante debe poder auditarse.
  4. La automatización nunca debe reducir la trazabilidad.
  5. Cuando exista incertidumbre alta, preguntar antes de actuar.
  6. La empresa siempre tiene prioridad sobre la comodidad del sistema.
  7. Los humanos siempre pueden anular una decisión.
  8. Toda decisión debe poder explicarse.
- Definición de los **niveles de autonomía**: Ejecutar, Proponer, Confirmar, Escalar.
- Definición del **modelo de aprendizaje supervisado** de CJ_OS.
- Actualización de `docs/CJ_OS_BLUEPRINT.md` con Nivel 10 — Filosofía y Constitución.
- Actualización de `docs/ROADMAP.md` para incluir M2.3.
- Actualización de `docs/PROJECT_BIBLE.md`:
  - Tabla de milestones con M2.3.
  - Estructura del Core actualizada con `behavior/`.
- Actualización de `core/README.md` para reflejar la quinta capa.
- Actualización de `docs/INSTALL_LOG.md`.
- **No se programó código.**
- **No se crearon tablas.**
- **No se crearon APIs.**
- **No se crearon módulos.**
- **No se tocó la base de datos.**

## Versión 0.0.14

**Fecha:** 2026-06-25

### Cambios realizados

- Aprobación del Milestone **M2.2 — Arquitectura Cognitiva**, propuesto por Carlos.
- Actualización de `docs/ROADMAP.md` para incluir M2.2 entre M2 y M3.
- Reestructuración de `docs/CJ_OS_BLUEPRINT.md` con nueva sección: **Nivel 8 — Arquitectura Cognitiva**.
- Definición del **Motor de Decisiones** (`core/decision_engine/`):
  - Responsable de clasificar eventos, evaluar contexto y decidir si actúa, pide confirmación o escala.
  - Ejemplo documentado: Francisco manda una foto.
- Definición del flujo de razonamiento en `core/reasoning/`:
  - Observación → Clasificación → Contexto → Reglas → Objetivos → Políticas → Evaluación → Acción → Auditoría.
- Definición del sistema de políticas en `core/policies/`:
  - Seguridad, prioridad, privacidad, automatización, costos, escalamiento, IA, backups.
- Definición de la separación entre:
  - **Datos:** hechos concretos.
  - **Conocimiento:** cómo funciona la empresa.
  - **Inteligencia:** capacidad de decidir qué hacer.
- Definición del **Consejo de Agentes**:
  - Agentes especializados: Arquitecto, Operaciones, Calidad, Compras, Ventas, Inventario, Automatización, RRHH, Dirección.
  - Una solicitud se enruta al agente más adecuado.
- Creación de carpetas en `core/`:
  - `core/decision_engine/`
  - `core/reasoning/`
  - `core/policies/`
- Creación de `README.md` en cada nueva carpeta del Core.
- Actualización de `core/README.md` para reflejar la Arquitectura Cognitiva.
- Actualización de `docs/PROJECT_BIBLE.md`:
  - Tabla de milestones con M2.2.
  - Estructura del Core actualizada.
- Actualización de `docs/INSTALL_LOG.md`.
- **No se programó código.**
- **No se crearon tablas.**
- **No se crearon APIs.**
- **No se crearon módulos.**
- **No se tocó la base de datos.**

## Versión 0.0.13

**Fecha:** 2026-06-25

### Cambios realizados

- Reestructuración completa del `docs/CJ_OS_BLUEPRINT.md` con capas superiores:
  - Nivel 0 — Visión.
  - Nivel 1 — Principios.
  - Nivel 2 — Dominios funcionales de la empresa.
  - Nivel 3 — Arquitectura general.
  - Nivel 4 — Motor de IA multi-modelo.
  - Nivel 5 — Memoria, conocimiento, reglas y objetivos.
  - Nivel 6 — Flujos principales.
  - Nivel 7 — Capacidades a 6 meses y 2 años.
  - Nivel 8 — Criterios de aprobación del Blueprint.
- Definición del **Motor de IA multi-modelo** con asignación inicial de tareas a proveedores (Kimi Code, ChatGPT, Gemini, Claude, Qwen, Ollama).
- Definición de los cuatro niveles de criterio: Memoria, Conocimiento, Reglas y Objetivos.
- Cambio de enfoque de "módulos" a "dominios funcionales de la empresa".
- Creación de carpetas en `core/`: `knowledge/`, `rules/`, `goals/`.
- Creación de `README.md` en `core/knowledge/`, `core/rules/` y `core/goals/`.
- Actualización de `core/README.md` y `core/memory/README.md` para reflejar los cuatro niveles.
- Actualización de `docs/ROADMAP.md` para reflejar el enfoque del Blueprint v1.0.
- Actualización de `docs/PROJECT_BIBLE.md`.
- Actualización de `docs/INSTALL_LOG.md`.
- **No se crearon tablas de PostgreSQL.**
- **No se programó código.**
- **No se crearon APIs.**
- **No se crearon módulos.**
- **No se tocó la base de datos.**

## Versión 0.0.12

**Fecha:** 2026-06-25

### Cambios realizados

- Aprobación del cambio de roadmap propuesto por Carlos.
- Reordenamiento oficial del roadmap:
  - M2 pasa de **Base de Datos** a **Arquitectura Funcional**.
  - M3 pasa a **Modelo de Datos**.
  - M4 pasa a **Integraciones**.
  - M5 pasa a **Automatización**.
  - M6 pasa a **IA**.
  - M7 pasa a **Producción**.
- Actualización completa de `docs/ROADMAP.md` con la nueva estructura de milestones.
- Actualización de `docs/PROJECT_BIBLE.md` con la tabla de milestones actualizada.
- Registro de la decisión arquitectónica en `docs/DECISIONS.md`.
- Actualización de `docs/INSTALL_LOG.md`.
- Creación de la estructura del documento maestro `docs/CJ_OS_BLUEPRINT.md`.
- **No se crearon tablas de PostgreSQL.**
- **No se programó código.**
- **No se crearon APIs.**
- **No se crearon módulos.**
- El proyecto queda enfocado en diseñar el dominio del negocio antes de implementar tecnología.

## Versión 0.0.11

**Fecha:** 2026-06-25

### Cambios realizados

- Inicio oficial de la **Fase M1.4 - Prueba de persistencia y reinicio controlado**, autorizado por Carlos.
- Creación de un workflow de prueba no productivo en n8n: "M1.4 Persistence Test".
- Registro del estado inicial: contenedores activos, 109 tablas en PostgreSQL y tamaños de `runtime/`.
- Apagado controlado de todos los servicios mediante `docker compose down`.
- Verificación de que todos los contenedores se detuvieron correctamente.
- Reinicio controlado de PostgreSQL, Redis y n8n mediante `docker compose up -d postgres redis n8n`.
- Verificación post-reinicio:
  - PostgreSQL healthy.
  - Redis healthy.
  - n8n accesible en `http://localhost:5678/` (HTTP 200).
  - Workflow de prueba persistente en n8n.
  - 109 tablas conservadas en PostgreSQL.
  - Datos de `runtime/n8n` y `runtime/database/redis` conservados.
- Verificación de logs: sin errores críticos (solo warning conocido del Python task runner en modo interno).
- Actualización de `docs/PROJECT_BIBLE.md`: Milestone M1 marcado como **Completado**.
- Actualización de `docs/INSTALL_LOG.md`.
- Creación del reporte `docs/reports/M1.4_persistence_restart_test.md`.
- **No se conectaron APIs externas.**
- **No se crearon workflows productivos.**
- **No se instalaron nodos adicionales.**
- **Milestone M1 (Infraestructura) oficialmente CERRADO.**
- Listo para iniciar el **Milestone M2** (Base de Datos).

## Versión 0.0.10

**Fecha:** 2026-06-25

### Cambios realizados

- Inicio oficial de la **Fase M1.3 - Despliegue inicial de n8n**, autorizado por Carlos.
- Revisión completa de `infrastructure/compose/docker-compose.yml` para validar configuración de n8n.
- Validación de variables de entorno necesarias para n8n en `.env`.
- Confirmación de que n8n utiliza **PostgreSQL** como base de datos (`DB_TYPE=postgresdb`), no SQLite.
- Confirmación de que Redis está preparado para futuras colas.
- Verificación de que todos los volúmenes de datos son persistentes (`runtime/database/postgres`, `runtime/database/redis`, `runtime/n8n`).
- Verificación de que las credenciales no están escritas directamente en `docker-compose.yml` (usan variables de entorno).
- Levantamiento exitoso del servicio `n8n` mediante `docker compose up -d n8n`.
- Verificación de que n8n responde correctamente en la interfaz web (`HTTP 200`).
- Confirmación de que n8n creó **109 tablas** en PostgreSQL.
- Creación del documento `docs/N8N_ARCHITECTURE.md` explicando función, responsabilidades y flujo de n8n dentro de CJ_OS.
- Registro de la decisión aritectónica en `docs/DECISIONS.md`.
- Actualización de `docs/PROJECT_BIBLE.md` para reflejar a n8n como orquestador.
- Actualización de `docs/INSTALL_LOG.md`.
- **No se crearon workflows.**
- **No se conectaron APIs.**
- **No se instalaron nodos adicionales.**
- **No se importaron proyectos.**
- Milestone M1 (Infraestructura) completado y validado.

## Versión 0.0.9

**Fecha:** 2026-06-25

### Cambios realizados

- Inicio oficial de la **Fase M1.2.5 - Preparación del Core de CJ_OS**, autorizado por Carlos.
- Aprobación del cambio arquitectónico mayor: **n8n = Orquestador, CJ_OS = Cerebro**.
- Creación de la estructura completa del Core en `core/`:
  - `core/api/`
  - `core/events/`
  - `core/scheduler/`
  - `core/memory/`
  - `core/audit/`
  - `core/security/`
  - `core/config/`
  - `core/utils/`
  - `core/orchestrator/`
- Creación de archivos `README.md` en cada componente del Core para documentar su propósito y responsabilidades.
- Creación del documento `docs/CORE_ARCHITECTURE.md` con:
  - Responsabilidades del Core.
  - Responsabilidades de n8n como orquestador.
  - Responsabilidades de los Connectors.
  - Responsabilidades de los módulos de negocio.
  - Flujo principal del sistema: WhatsApp → n8n → Core → IA → Módulo → PostgreSQL → Respuesta.
- Registro de la decisión arquitectónica en `docs/DECISIONS.md`.
- Actualización de `docs/PROJECT_BIBLE.md` para reflejar:
  - El Core como cerebro del sistema.
  - La nueva estructura de carpetas del Core.
  - El flujo general de datos.
  - El principio "n8n = Orquestador, CJ_OS = Cerebro".
- **No se escribió código.**
- **No se crearon APIs.**
- **No se instalaron dependencias.**
- **No se modificó PostgreSQL ni Redis.**
- **No se inició n8n.**
- En espera de autorización del Product Owner para iniciar la **Fase M1.3** (n8n).

## Versión 0.0.8

**Fecha:** 2026-06-25

### Cambios realizados

- Inicio oficial de la **Fase M1.2 - Validación de PostgreSQL y Redis**, autorizado por Carlos.
- Revisión del archivo `infrastructure/compose/docker-compose.yml` para validar la definición de los servicios `postgres` i `redis`.
- Levantamiento controlado de únicamente PostgreSQL y Redis mediante `docker compose up -d postgres redis`.
- Descarga exitosa de las imágenes `postgres:16-alpine` i `redis:7-alpine` desde Docker Hub.
- Creación correcta de la red `cj_network`.
- Verificación de healthchecks: ambos contenedores reportan estado `healthy`.
- Validación de PostgreSQL mediante consulta `SELECT version();` — responde `PostgreSQL 16.14`.
- Validación de Redis mediante `redis-cli ping` — responde `PONG` con autenticación activa.
- Revisión de uso de recursos: uso eficiente de RAM y CPU.
- Generación del reporte oficial `docs/reports/M1.2_postgres_redis_validation.md` con estado **VALIDADA**.
- Registro detallado en `docs/INSTALL_LOG.md`.
- **No se inició n8n.**
- **No se modificó la arquitectura.**
- **No se instalaron componentes adicionales.**
- En espera de autorización del Product Owner para iniciar la **Fase M1.3** (n8n).

## Versión 0.0.7

**Fecha:** 2026-06-25

### Cambios realizados

- Inicio oficial de la **Fase M1.1 - Validación de Docker**.
- Actualización de WSL a la versión más reciente mediante `wsl --update` para resolver el aviso de versión obsoleta detectado por Docker Desktop.
- Reinicio controlado de Docker Desktop y verificación de respuesta del Docker Engine.
- Validación exitosa de Docker Engine `29.5.3`, Docker Desktop `4.79.0` y Docker Compose `v5.1.4`.
- Verificación de funcionamiento de WSL2 con la distribución `docker-desktop` en ejecución.
- Ejecución de contenedor de prueba `hello-world` con descarga exitosa desde Docker Hub.
- Generación del reporte oficial `docs/reports/M1.1_docker_validation.md` con estado **VALIDADA**.
- Registro detallado en `docs/INSTALL_LOG.md`.
- **No se iniciaron n8n, PostgreSQL ni Redis.**
- **No se descargaron imágenes adicionales más allá de `hello-world`.**
- En espera de autorización del Product Owner para iniciar la **Fase M1.2**.

## Versión 0.0.6

**Fecha:** 2026-06-25

### Cambios realizados

- Incorporación de la retroalimentación arquitectónica de ChatGPT.
- Reestructuración de `PROJECT_BIBLE.md` para reflejar la arquitectura CJ_OS v1.0 con `core/`, `ai/`, `connectors/`, `modules/`, `workspace/` y `runtime/`.
- Actualización de `ENVIRONMENT.md` con variables para `core/`, `connectors/`, `runtime/`, `config/` por ambiente y activación de agentes.
- Registro en `DECISIONS.md` de las decisiones arquitectónicas clave v1.0: fuentes de verdad duales, Event Bus, capa `core/`, `connectors/`, `ai/`, `runtime/`, configuración por ambiente y agentes especializados.
- Refuerzo de la decisión de **no instalar Docker hasta que Carlos apruebe la arquitectura v1.0**.

## Versión 0.0.5

**Fecha:** 2026-06-25

### Cambios realizados

- Revisión y aprobación conceptual de la arquitectura **CJ_OS v1.0**.
- Creación de `ARCHITECTURE.md` con la visión, componentes, módulos, flujo de datos y estructura definitiva.
- Rediseño de `SYSTEM_MAP.md` con el diagrama arquitectónico de CJ_OS.
- Actualización de `PROJECT_BIBLE.md` con arquitectura modular, componentes, módulos de negocio y abstracción de IA.
- Actualización de `ENVIRONMENT.md` con variables para proveedor de IA (`IA_PROVIDER`) y activación de módulos.
- Actualización de `ROADMAP.md` con las fases ampliadas del proyecto.
- Decisión de **no instalar Docker todavía** hasta que la arquitectura quede completamente definida.
- Decisión de diseñar CJ_OS como sistema operativo inteligente para 3P, no solo un asistente.
- Decisión de dividir el sistema en módulos de negocio independientes.
- Decisión de hacer el sistema independiente del proveedor de IA.

## Versión 0.0.4

**Fecha:** 2026-06-26

### Cambios realizados

- Movimiento de la carpeta del proyecto a la ubicación definitiva de desarrollo: `C:\Projects\CJ_Assistant\`.
- Actualización de `ROLLBACK_PLAN.md` para reflejar la nueva ubicación del proyecto.
- Actualización de `PROJECT_BIBLE.md` y `SYSTEM_MAP.md` para indicar la nueva ubicación.
- Registro en `DECISIONS.md` del cambio de ubicación y sus implicaciones.

## Versión 0.0.3

**Fecha:** 2026-06-25

### Cambios realizados

- Inicio del **Milestone M1.0.1 - Revisión de Arquitectura**, autorizado por Carlos.
- Diseño de la estructura definitiva de carpetas para la versión 1.0.
- Creación de `ENVIRONMENT.md` con el catálogo completo de variables de entorno.
- Actualización de `PROJECT_BIBLE.md` con la arquitectura general y la estructura de carpetas definitiva.
- Actualización de `SYSTEM_MAP.md` con el diagrama ASCII de la arquitectura propuesta.
- Registro en `DECISIONS.md` de las decisiones arquitectónicas clave: separación de carpetas, configuración por `.env` y persistencia en OneDrive.

## Versión 0.0.2

**Fecha:** 2026-06-25

### Cambios realizados

- Inicio oficial del **Milestone M1 - Infraestructura**, autorizado por Carlos.
- Creación del plan de instalación (`INSTALL_PLAN.md`) para Docker, n8n, PostgreSQL y Redis.
- Creación del plan de rollback (`ROLLBACK_PLAN.md`) con pasos para revertir la instalación.
- Creación del registro de instalación (`INSTALL_LOG.md`).
- Actualización del estado de los Milestones en `PROJECT_BIBLE.md`.

## Versión 0.0.1

**Fecha:** 2026-06-25

### Cambios realizados

- Creación de la estructura base del proyecto.
- Preparación de la carpeta de documentación maestra.
- Inicialización de plantillas de documentación.
- Definición oficial del rol de Kimi como Ingeniero DevOps del proyecto.
- Registro de la metodología por Milestones con validación de Carlos.
- Definición de los tres roles del proyecto: Carlos (Product Owner), Kimi (DevOps) y ChatGPT (Arquitecto).
- Documentación de la propuesta de renombrar el proyecto a CJ_OS en la versión estable v1.0.
