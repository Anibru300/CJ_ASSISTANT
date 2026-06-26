# Roadmap - CJ_OS

**Versión:** 0.0.25  
**Fecha de actualización:** 2026-06-25  
**Estado:** Roadmap oficial aprobado por Carlos

---

## Principio rector

> Primero diseñamos el dominio del negocio. Después implementamos la tecnología.

Este roadmap sigue el orden lógico de empresas grandes: **diseño funcional antes de modelo de datos, y modelo de datos antes de código.**

---

## Milestone M0 - Preparación del entorno ✅

- Preparar estructura base del proyecto.
- Configurar Python y herramientas base.
- Realizar limpieza conservadora del entorno.

**Estado:** Completado.

---

## Milestone M1 - Infraestructura ✅

- Instalar Docker Desktop.
- Configurar Docker Desktop con límites de recursos.
- Crear `docker-compose.yml` con n8n, PostgreSQL y Redis.
- Levantar servicios base.
- Verificar conectividad entre contenedores.
- Validar persistencia y reinicio controlado.

**Estado:** Completado.

---

## Milestone M2 - Arquitectura Funcional ✅

**Objetivo:** Definir qué es CJ_OS antes de escribir código, crear tablas o conectar APIs.

### Entregable principal

- **`docs/CJ_OS_BLUEPRINT.md`** — Blueprint maestro del sistema.

### Actividades

- Definir la visión de CJ_OS como Sistema Operativo Empresarial.
- Identificar dominios funcionales de la empresa.
- Identificar usuarios y roles.
- Definir permisos por usuario y por dominio.
- Definir tipos de información que guardará CJ_OS.
- Diseñar el flujo de comunicación entre dominios, canales, IA y memoria.
- Definir estrategia de proveedores de IA intercambiables.
- Definir capacidades futuras a 6 meses y 2 años.
- Validar el Blueprint con Carlos antes de avanzar.

**Estado:** Completado.

---

## Milestone M2.1 - Filosofía de CJ_OS ✅

**Objetivo:** Definir el ADN de CJ_OS antes de construir el Modelo de Datos.

### Entregable principal

- **`docs/CJ_OS_PHILOSOPHY.md`** — documento conceptual del comportamiento y valores de CJ_OS.
- Quinta capa del Core: `core/behavior/`.

### Actividades

- Definir la misión de CJ_OS.
- Establecer los valores del sistema.
- Definir el comportamiento profesional.
- Redactar la Constitución de CJ_OS.
- Definir niveles de autonomía A0-A5.
- Definir modelo de aprendizaje supervisado.
- Validar la Filosofía con Carlos antes de avanzar.

**Estado:** Completado.

---

## Milestone M2.2 - Blueprint ✅

**Objetivo:** Definir qué es CJ_OS, sus dominios, su arquitectura y su motor de IA antes de escribir código, crear tablas o conectar APIs.

### Entregable principal

- **`docs/CJ_OS_BLUEPRINT.md`** — Blueprint maestro del sistema.

### Actividades

- Definir la visión de CJ_OS como Sistema Operativo Empresarial.
- Identificar dominios funcionales de la empresa.
- Identificar usuarios y roles.
- Definir permisos por usuario y por dominio.
- Diseñar el flujo de comunicación entre dominios, canales, IA y memoria.
- Definir estrategia de proveedores de IA intercambiables.
- Definir capacidades futuras a 6 meses y 2 años.
- Validar el Blueprint con Carlos antes de avanzar.

**Estado:** Completado.

---

## Milestone M2.3 - Modelo Operativo de la Empresa 🔄

**Objetivo:** Crear el primer borrador del modelo operativo de 3P como insumo para los catálogos de conocimiento.

### Entregable principal

- **`docs/CJ_OS_OPERATING_MODEL.md`** — modelo operativo maestro de la empresa (borrador base).

### Actividades

- Identificar los roles actuales de 3P y sus responsabilidades.
- Mapear procesos críticos por dominio funcional.
- Definir permisos de lectura/escritura/aprobación por rol y dominio.
- Documentar flujos de decisión frecuentes.
- Vincular el Modelo Operativo con el Blueprint y la Filosofía.

**Estado:** Borrador base completado. Se enriquecerá durante M2.8.

---

## Milestone M2.4 - Auditoría y Aprobación Documental 🔄

**Objetivo:** Validar que la documentación de arquitectura y diseño sea clara, consistente y suficiente antes de construir el Modelo de Datos.

### Entregable principal

- **`docs/reports/M2.4_documentation_audit.md`** — reporte de auditoría documental.

### Actividades

- Revisar consistencia entre Blueprint, Filosofía, Roadmap, Decisiones, System Map y Core Architecture.
- Corregir referencias desactualizadas (número de capas, componentes del Core, estados de milestones).
- Decidir destino de documentos obsoletos o redundantes.
- Obtener aprobación formal de Carlos para cerrar M2.4.

**Estado:** Auditoría completada. En espera de aprobación de Carlos.

---

## Milestone M2.5 - Ontología Empresarial ⏳

**Objetivo:** Definir qué existe en 3P, cómo se llama, qué significa, qué atributos tiene y qué restricciones tiene cada entidad. Será la fuente semántica del modelo de datos.

### Entregable principal

- **`docs/CJ_OS_ONTOLOGY.md`** — ontología empresarial de 3P.

### Actividades

- Identificar entidades por dominio (Producto, Rack, Vale, OC, Proveedor, Cliente, etc.).
- Definir atributos de cada entidad.
- Definir relaciones entre entidades.
- Definir restricciones y reglas de integridad.
- Validar con Carlos antes de avanzar.

**Estado:** Pendiente.

---

## Milestone M2.6 - Catálogo de Eventos ⏳

**Objetivo:** Documentar todos los eventos de negocio que alimentarán el Event Bus, n8n, los agentes y la auditoría.

### Entregable principal

- **`docs/CJ_OS_EVENT_CATALOG.md`** — catálogo de eventos empresariales.

### Actividades

- Nombrar eventos en formato `sustantivo_verbo` (ej. `llego_mercancia`, `se_creo_vale`).
- Definir qué información lleva cada evento.
- Identificar qué proceso genera cada evento.
- Identificar qué proceso consume cada evento.
- Validar con Carlos antes de avanzar.

**Estado:** Pendiente.

---

## Milestone M2.7 - Catálogo de Decisiones ⏳

**Objetivo:** Documentar las decisiones reales que ocurren en cada dominio: qué información necesitan, quién las toma y qué resultados pueden tener.

### Entregable principal

- **`docs/CJ_OS_DECISION_CATALOG.md`** — catálogo de decisiones empresariales.

### Actividades

- Identificar decisiones clave por dominio.
- Documentar información necesaria para decidir.
- Definir posibles resultados de cada decisión.
- Asignar actor responsable y nivel de autonomía A0-A5.
- Validar con Carlos antes de avanzar.

**Estado:** Pendiente.

---

## Milestone M2.8 - Catálogo de Reglas ⏳

**Objetivo:** Documentar las reglas de negocio de forma explícita, separada y accionable. Cada regla será una futura validación automática.

### Entregable principal

- **`docs/CJ_OS_RULES_CATALOG.md`** — catálogo de reglas de negocio.

### Actividades

- Extraer reglas de cada dominio.
- Clasificar reglas por tipo (integridad, autorización, flujo, excepción).
- Asignar prioridad y evento relacionado.
- Definir si la regla puede romperse y quién puede autorizarlo.
- Validar con Carlos antes de avanzar.

**Estado:** Pendiente.

---

## Milestone M2.9 - Business Knowledge Acquisition (BKA) ⏳

**Nombre alternativo:** Fase de Adquisición del Conocimiento Empresarial.

**Sesiones:** Knowledge Engineering Sessions (KES) / Sesiones de Ingeniería del Conocimiento (SIC).

**Objetivo:** Extraer conocimiento experto de cada área de 3P para completar el Business Dictionary, la Ontología, el Knowledge Graph, los catálogos de eventos/decisiones/reglas, el Cognitive Model y el Modelo Operativo. No se escribe una sola tabla de base de datos hasta que todo el conocimiento esté adquirido, validado, gobernado y medido con la **Knowledge Coverage Matrix**.

### Condición previa a la primera KES de dominio

Antes de entrevistar a Francisco o Salvador, se debe:

1. Establecer la **Document Governance** (`CJ_OS_DOCUMENT_GOVERNANCE.md`).
2. Crear el **Business Dictionary** con los términos transversales.
3. Crear el **Cognitive Model** como manual de pensamiento.
4. Ejecutar la **KES-0 — Lenguaje Empresarial**.

> Sin KES-0 aprobada, no inicia ninguna sesión de dominio.

### Entregables principales

- **`docs/CJ_OS_CANON.md`** — documentos oficiales y jerarquía de resolución de conflictos.
- **`docs/CJ_OS_DOCUMENT_GOVERNANCE.md`** — reglas de documentos maestros, derivados y temporales.
- **`docs/CJ_KNOWLEDGE_ACQUISITION_PROTOCOL.md`** — protocolo formal de extracción de conocimiento.
- **`docs/CJ_KNOWLEDGE_COVERAGE_MATRIX.md`** — matriz de cobertura por dominio y categoría.
- **`docs/CJ_OS_KNOWLEDGE_EVIDENCE_STANDARD.md`** — estándar de evidencia para cada conocimiento.
- **`docs/CJ_OS_BUSINESS_DICTIONARY.md`** — diccionario empresarial de términos oficiales.
- **`docs/CJ_OS_COGNITIVE_MODEL.md`** — manual de pensamiento de CJ_OS.
- **`docs/CJ_OS_KNOWLEDGE_GRAPH.md`** — grafo de conocimiento con relaciones entre entidades.
- **`docs/CJ_OS_OPERATING_MODEL.md`** — modelo operativo con conocimiento empresarial validado por dominio.
- **`docs/reports/M2.8_business_knowledge_acquisition.md`** — registro de KES/SIC, decisiones, excepciones y aprobaciones por dominio.

### Fases de M2.8

1. **Preparación metodológica en Evolución Controlada**
   - Aprobar Canon y Document Governance.
   - Aprobar KAP, Coverage Matrix, Evidence Standard, Definition of Done y Traceability Matrix.
   - Crear Business Dictionary y Cognitive Model.
   - Crear registros `Known Unknowns` y `Assumptions Register`.
   - Ejecutar **KES-Pilot** modelando un solo proceso real (entrada de mercancía de proveedor).
   - **Cerrar fase de diseño:** no se crean más documentos metodológicos hasta completar al menos 3 KES reales.
   - **No declarar Architecture Freeze** hasta después de validar Almacén, Compras, Ventas y Logística.
2. **KES-0 — Lenguaje Empresarial**
   - Validar términos transversales con Carlos y líderes de área.
3. **KES/SIC 1–9 — Dominios operativos**
   - Extraer, revisar, aprobar y consolidar conocimiento por dominio.

### Sesiones propuestas

0. **KES/SIC 0 — Lenguaje Empresarial** (condición previa obligatoria).
1. **KES/SIC 1 — Almacén** (prioridad alta, patrón de referencia).
2. **KES/SIC 2 — Compras**.
3. **KES/SIC 3 — Logística**.
4. **KES/SIC 4 — Calidad**.
5. **KES/SIC 5 — Ventas**.
6. **KES/SIC 6 — Contabilidad**.
7. **KES/SIC 7 — RRHH**.
8. **KES/SIC 8 — Inteligencia Empresarial**.
9. **KES/SIC 9 — Dirección y procesos transversales**.

### Estructura de cada sesión

Cada sesión extraerá conocimiento experto usando la ficha maestra del dominio:

1. **Objetivo** — ¿para qué existe el dominio?
2. **AS-IS** — ¿cómo trabaja la empresa hoy?
3. **TO-BE** — ¿cómo debería trabajar con CJ_OS en un año?
4. **Automatización futura** — ¿qué hará CJ_OS automáticamente?
5. **Actores** — ¿quién participa?
6. **Objetos** — ¿qué entidades existen?
7. **Eventos** — ¿qué cosas pueden ocurrir?
8. **Procesos** — cada proceso responde 5 preguntas: ¿qué lo inicia?, ¿qué lo termina?, ¿qué consume?, ¿qué produce?, ¿qué evento genera?
9. **Reglas** — ¿qué nunca debe violarse?
10. **Conocimiento semántico** — hechos, reglas, heurísticas y excepciones.
11. **Excepciones** — ¿qué pasa cuando algo falla?
12. **Decisiones** — ¿quién decide qué?
13. **KPIs** — ¿cómo medimos?
14. **Matriz de madurez** — documentado, estandarizado, automatizable, automatizado.
15. **Pregunta final:** *¿Qué haría el mejor gerente de esta área que hoy nadie hace?*

### Actividades por sesión

- Entrevistar al experto del dominio (no solo documentar).
- Extraer objetos, relaciones, eventos, procesos, decisiones y reglas.
- **Registrar todo en notas temporales; NO editar documentos maestros durante la entrevista.**
- Revisar las notas, depurar ambigüedades y obtener aprobación del responsable.
- Consolidar solo lo aprobado en los documentos maestros correspondientes.
- Construir fragmentos del Knowledge Graph para el dominio.
- Documentar excepciones y reglas de contingencia.
- Clasificar cada pieza de conocimiento como hecho, regla, heurística o excepción.
- Asignar capa (permanente / operativo / estratégico) y criticalidad (crítica / alta / media / baja).
- Registrar fuente, fecha, estado, nivel de confianza y **evidencia** de cada ítem.
- Ejecutar los cuatro tipos de sesión según sea necesario: **KES-D, KES-I, KES-O, KES-V**.
- Mantener actualizados `Known Unknowns` y `Assumptions Register`.
- Actualizar el **Business Dictionary** si emergen nuevos términos.
- Construir la matriz de madurez del dominio.
- Actualizar la **Knowledge Coverage Matrix** tras cada sesión.
- Capturar oportunidades de inteligencia: *¿qué haría el mejor gerente?*
- Validar y aprobar el conocimiento del dominio antes de pasar al siguiente.

**Estado:** Pendiente. No iniciar M3 hasta que todas las sesiones estén aprobadas.

---

## Milestone M3 - Modelo de Datos ⏳

**Objetivo:** Traducir la Ontología, el Knowledge Graph y el conocimiento adquirido en M2.8 a un modelo de datos estructurado.

### Actividades

- Diseñar esquema de PostgreSQL basado en el Blueprint y el Modelo Operativo validado.
- Definir entidades, relaciones, índices y restricciones.
- Crear tablas base.
- Configurar respaldos automáticos.
- Validar persistencia en `runtime/database/`.

**Estado:** Pendiente. No iniciar hasta aprobación de Ontología + Knowledge Graph + Catálogos de Eventos/Decisiones/Reglas + Modelo Operativo + BKA.

---

## Milestone M4 - Integraciones ⏳

**Objetivo:** Conectar CJ_OS con los sistemas externos que ya utiliza 3P.

### Actividades

- Conectar WhatsApp.
- Conectar Outlook.
- Conectar OneDrive.
- Conectar Google Drive.
- Conectar SAE (Aspel).
- Conectar Excel de almacén.
- Validar cada conector de forma aislada.

**Estado:** Pendiente.

---

## Milestone M5 - Automatización ⏳

**Objetivo:** Configurar n8n como orquestador de flujos de negocio.

### Actividades

- Crear workflows base.
- Integrar Scheduler para tareas recurrentes.
- Implementar logging centralizado.
- Conectar workflows con el Core de CJ_OS.

**Estado:** Pendiente.

---

## Milestone M6 - IA ⏳

**Objetivo:** Implementar la capa de inteligencia artificial con abstracción de proveedores.

### Actividades

- Implementar adaptador de IA.
- Soportar múltiples proveedores: OpenAI, Kimi, Claude, Gemini, Qwen, DeepSeek.
- Crear Prompt Manager por módulo.
- Implementar memoria conversacional.
- Implementar transcripción de voz a texto.
- Definir motor de decisiones del Core.

**Estado:** Pendiente.

---

## Milestone M7 - Producción ⏳

**Objetivo:** Preparar CJ_OS para operación estable y segura.

### Actividades

- Auditoría de seguridad.
- Cifrado de credenciales.
- Estrategia de respaldos robusta.
- Documentación de operación.
- Plan de contingencia.
- Pruebas finales.
- Validación con usuarios clave.
- Renombrar proyecto a **CJ_OS**.
- Puesta en producción.

**Estado:** Pendiente.

---

## Notas de evolución

| Fecha | Cambio | Motivo |
|-------|--------|--------|
| 2026-06-25 | Se reordenó el roadmap: M2 pasó de "Base de Datos" a "Arquitectura Funcional". | Evitar construir infraestructura sin inteligencia. Definir el dominio del negocio antes de implementar tecnología. |
| 2026-06-25 | Se creó el entregable `docs/CJ_OS_BLUEPRINT.md` como documento maestro del sistema. | Servir como fuente de verdad funcional antes de desarrollar código, APIs o tablas. |
| 2026-06-25 | Se agregó el Milestone M2.2 — Arquitectura Cognitiva entre M2 y M3. | Definir cómo piensa CJ_OS (motor de decisiones, razonamiento, políticas, Consejo de Agentes) antes del modelo de datos. |
| 2026-06-25 | Se agregó el Milestone M2.3 — Filosofía y Constitución de CJ_OS entre M2.2 y M3. | Definir el ADN del sistema (misión, valores, comportamiento, constitución, autonomía) antes de desarrollar tecnología. |
| 2026-06-25 | Se agregó el Milestone M2.4 — Auditoría y Aprobación Documental entre M2.3 y M3. | Validar que la documentación sea clara, consistente y suficiente antes de construir el Modelo de Datos. |
| 2026-06-25 | Se cerró M2.4 y se agregó el Milestone M2.5 — Modelo Operativo de la Empresa antes de M3. | Definir procesos, roles y permisos del negocio antes de diseñar tablas. |
| 2026-06-25 | Se agregó el Milestone M2.6 — Business Design Review tras M2.5. | Validar dominio por dominio que CJ_OS entienda exactamente cómo funciona 3P antes del Modelo de Datos. |
| 2026-06-25 | Se renombró M2.6 a **Business Knowledge Acquisition (BKA)**. | El foco no es solo validar, sino adquirir el conocimiento empresarial que CJ_OS necesita para operar. |
| 2026-06-25 | Se agregaron tres versiones por dominio: AS-IS, TO-BE y Automatización futura. | Tener visión de evolución del negocio, no solo documentación del presente. |
| 2026-06-25 | Se agregaron secciones de conocimiento, excepciones y matriz de madurez por dominio. | Capturar reglas semánticas, contingencias y nivel de madurez real de cada proceso. |
| 2026-06-25 | Se estableció meta explícita: separar el motor de CJ_OS del conocimiento específico de cada empresa. | Permitir reutilizar la plataforma en otras empresas cambiando solo el conocimiento del negocio. |
| 2026-06-25 | Se ajustaron los dominios funcionales a 9 dominios operativos de 3P. | Reflejar la estructura real de la empresa: Dirección, Ventas, Compras, Almacén, Logística, Calidad, Contabilidad, RRHH e Inteligencia Empresarial. |
| 2026-06-25 | Se adoptó la estructura de fichas maestras por dominio. | Documentar objetivo, actores, objetos, eventos, procesos, reglas, decisiones, KPIs y automatizaciones para que el Modelo de Datos surja casi automáticamente. |
| 2026-06-25 | **Reorganización metodológica de M2:** M2.1 Filosofía, M2.2 Blueprint, M2.3 Modelo Operativo, M2.4 Ontología, M2.5 Eventos, M2.6 Decisiones, M2.7 Reglas, M2.8 BKA/KES. | Crear una metodología sistemática de adquisición de conocimiento antes de construir el modelo de datos. |
| 2026-06-25 | Se creó `docs/CJ_OS_FRAMEWORK.md` como metodología reutilizable. | Documentar el marco de trabajo que permite implementar CJ_OS en otras empresas cambiando solo el conocimiento del negocio. |
| 2026-06-25 | Se renombraron las sesiones a **Knowledge Engineering Sessions (KES)** / Sesiones de Ingeniería del Conocimiento (SIC). | Reflejar que el trabajo es extracción de conocimiento experto, no solo entrevistas o documentación. |
| 2026-06-25 | Se crearon documentos de Ontología, Knowledge Graph, Catálogo de Eventos, Catálogo de Decisiones y Catálogo de Reglas como entregables de M2. | Convertir el conocimiento empresarial en activos documentales reutilizables y fuente del modelo de datos. |
| 2026-06-25 | **Versión 0.0.18.** Se crearon `docs/CJ_KNOWLEDGE_ACQUISITION_PROTOCOL.md` y `docs/CJ_KNOWLEDGE_COVERAGE_MATRIX.md` como entregables previos a la KES 1. | Estandarizar la extracción de conocimiento y medir el cierre de cada sesión por cobertura, no por tiempo. |
| 2026-06-25 | **Versión 0.0.19.** Se agregaron `CJ_OS_BUSINESS_DICTIONARY.md`, `CJ_OS_COGNITIVE_MODEL.md`, `CJ_OS_DOCUMENT_GOVERNANCE.md` y la KES-0 de Lenguaje Empresarial como condición previa. | Evitar ambigüedad de vocabulario, controlar el ciclo de vida del conocimiento y establecer gobernanza documental antes de la primera sesión de dominio. |
| 2026-06-25 | **Versión 0.0.20.** Se agregaron `CJ_OS_CANON.md`, `CJ_OS_KNOWLEDGE_EVIDENCE_STANDARD.md`, tipos de sesión KES-D/I/O/V, activos de conocimiento y arquitectura de tres niveles de información (Core / PostgreSQL / Data Lake). | Garantizar que todo conocimiento tenga evidencia, definir la verdad oficial y separar estratégico, operativo y evidencia para escalar. |
| 2026-06-25 | **Versión 0.0.21.** Se agregó `Architecture Freeze`, métricas de calidad del conocimiento, registros `Known Unknowns` y `Assumptions Register`, y rol de Kimi como auditor técnico. | Evitar deuda documental, medir éxito por conocimiento validado y mantener coherencia durante las KES. |
| 2026-06-25 | **Versión 0.0.22.** Reemplazado `Architecture Freeze` por `Controlled Evolution`; agregados KES-Pilot, naturaleza del conocimiento (universal/específico/estratégico) y estabilidad (estable/variable/temporal/experimental). | Mantener flexibilidad metodológica durante las primeras sesiones hasta validar dominios clave. |
| 2026-06-25 | **Versión 0.0.23.** Agregados `CJ_OS_DEFINITION_OF_DONE.md`, `CJ_OS_TRACEABILITY_MATRIX.md`, estados Baseline y regla de un propósito por documento. | Definir cuándo un documento está terminado, trazar impacto de cambios y evitar documentación innecesaria. |
| 2026-06-25 | **Versión 0.0.24.** KES-Pilot enfocada a modelar un solo proceso real; agregadas métricas de densidad y reutilización; cuatro preguntas post-KES; cierre de fase de diseño y rol de Kimi como auditor/modelador. | Demostrar que la metodología funciona en la práctica, no solo en papel. |
| 2026-06-25 | **Versión 0.0.25.** Agregado Knowledge Quality Score (KQS), ciclo de vida extendido del conocimiento, separación observación/patrón/buena práctica/regla, pregunta de sabiduría obligatoria y regla estricta de no cambios metodológicos durante las primeras 3 KES. | Medir calidad del conocimiento, evitar institucionalizar costumbres prematuramente y cerrar definitivamente la fase de diseño. |
