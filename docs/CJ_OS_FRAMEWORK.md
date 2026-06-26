# CJ_OS Framework

**Versión:** 0.4.0  
**Fecha:** 2026-06-25  
**Estado:** Documento metodológico  
**Propósito:** Definir la metodología reutilizable para implementar CJ_OS en cualquier empresa, separando el motor del sistema del conocimiento específico del negocio.

---

## 1. Principio fundamental

> **El motor de CJ_OS es genérico. El conocimiento del negocio es intercambiable.**

Esto significa que una misma plataforma (eventos, decisiones, memoria, agentes, seguridad, auditoría) puede operar diferentes empresas cambiando únicamente los documentos de conocimiento.

---

## 2. Flujo metodológico

```text
CJ_OS Framework
       │
       ▼
Canon
       │
       ▼
Document Governance
       │
       ▼
Knowledge Evidence Standard
       │
       ▼
Business Dictionary
       │
       ▼
Blueprint
       │
       ▼
Business Ontology
       │
       ▼
Operating Model
       │
       ▼
Knowledge Graph
       │
       ▼
Decision Catalog
       │
       ▼
Business Rules
       │
       ▼
Event Catalog
       │
       ▼
Data Model
       │
       ▼
Automation
       │
       ▼
AI
```

---

## 3. Descripción de cada capa

| Capa | Documento | Pregunta que responde |
|------|-----------|----------------------|
| **Framework** | `docs/CJ_OS_FRAMEWORK.md` | ¿Cómo se implementa CJ_OS en cualquier empresa? |
| **Canon** | `docs/CJ_OS_CANON.md` | ¿Qué documentos son la verdad oficial? |
| **Document Governance** | `docs/CJ_OS_DOCUMENT_GOVERNANCE.md` | ¿Qué documentos son maestros, derivados o temporales? |
| **Knowledge Evidence Standard** | `docs/CJ_OS_KNOWLEDGE_EVIDENCE_STANDARD.md` | ¿Qué evidencia respalda cada conocimiento? |
| **Definition of Done** | `docs/CJ_OS_DEFINITION_OF_DONE.md` | ¿Cuándo un documento se considera terminado? |
| **Business Dictionary** | `docs/CJ_OS_BUSINESS_DICTIONARY.md` | ¿Qué significa cada término oficial? |
| **Blueprint** | `docs/CJ_OS_BLUEPRINT.md` | ¿Qué es CJ_OS y cómo está construido? |
| **Ontología** | `docs/CJ_OS_ONTOLOGY.md` | ¿Qué entidades existen, qué atributos tienen y qué restricciones tienen? |
| **Operating Model** | `docs/CJ_OS_OPERATING_MODEL.md` | ¿Cómo opera el negocio hoy y cómo debería operar con CJ_OS? |
| **Knowledge Graph** | `docs/CJ_OS_KNOWLEDGE_GRAPH.md` | ¿Cómo se relacionan las entidades entre sí? |
| **Decision Catalog** | `docs/CJ_OS_DECISION_CATALOG.md` | ¿Qué decisiones se toman, quién las toma y con qué información? |
| **Rules Catalog** | `docs/CJ_OS_RULES_CATALOG.md` | ¿Qué reglas de negocio deben cumplirse? |
| **Event Catalog** | `docs/CJ_OS_EVENT_CATALOG.md` | ¿Qué eventos ocurren en el negocio? |
| **Data Model** | PostgreSQL (M3) | ¿Cómo se materializan las entidades y relaciones en tablas? |
| **Automation** | n8n + Core (M5) | ¿Cómo se automatizan los flujos? |
| **Cognitive Model** | `docs/CJ_OS_COGNITIVE_MODEL.md` | ¿Cómo decide, pregunta, ejecuta, propone o escala CJ_OS? |
| **Traceability Matrix** | `docs/CJ_OS_TRACEABILITY_MATRIX.md` | ¿Quién usa cada elemento de conocimiento? |
| **AI** | Agentes + Motor de IA (M6) | ¿Cómo decide y aprende CJ_OS? |

---

### 3.1 Regla de un propósito por documento

Cada documento debe responder **una pregunta concreta**. Si un documento responde varias preguntas o ninguna en particular, probablemente está mezclando responsabilidades y debería dividirse o fusionarse.

---

## 4. Knowledge Engineering Sessions (KES / SIC)

Las sesiones de adquisición de conocimiento no son entrevistas. Son sesiones de **extracción estructurada de conocimiento experto** donde un Knowledge Engineer (en este caso, CJ_OS junto con Carlos) extrae de los expertos del negocio.

### KES-0 — Lenguaje Empresarial (previo a cualquier dominio)

Antes de las sesiones por área se realiza una sesión de lenguaje para definir:

- Términos oficiales → Business Dictionary.
- Sinónimos aceptados y significados excluidos.
- Propietarios de cada término.

### KES 1–9 — Dominios operativos

Cada sesión de dominio alimenta:

- Objetos y atributos → Ontología.
- Relaciones → Knowledge Graph.
- Eventos → Event Catalog.
- Decisiones → Decision Catalog.
- Reglas → Rules Catalog.
- Procesos, excepciones, KPIs → Operating Model.
- Comportamiento de decisión → Cognitive Model.

### Ficha maestra por dominio

Cada KES completa una ficha con 15 secciones:

1. Objetivo
2. AS-IS
3. TO-BE
4. Automatización futura
5. Actores
6. Objetos
7. Eventos
8. Procesos (5 preguntas)
9. Reglas
10. Lo que CJ_OS debe saber
11. Excepciones
12. Decisiones
13. KPIs
14. Matriz de madurez
15. Pregunta final

---

## 5. Reutilización en otra empresa

Para adaptar CJ_OS a una nueva empresa, se repite el flujo:

1. Conservar el **motor** (Core, n8n, IA, infraestructura).
2. Empaquetar el **conocimiento** en un **Knowledge Pack**: Business Dictionary, Ontología, Operating Model, Knowledge Graph, catálogos, Cognitive Model.
3. Generar nuevo **Data Model** a partir de la ontología.
4. Configurar nuevas **automatizaciones** y **agentes**.

El motor no cambia. Solo cambia el Knowledge Pack.

---

## 6. Criterios de madurez del framework

- [ ] Los documentos de conocimiento son independientes del motor.
- [ ] Cada documento tiene formato estándar y versionado.
- [ ] Las KES producen actualizaciones medibles en los documentos.
- [ ] El Data Model puede generarse a partir de la Ontología y el Knowledge Graph.
- [ ] Los workflows de n8n pueden generarse a partir del Event Catalog y los procesos.

---

## Historial de cambios

| Fecha | Versión | Cambio |
|-------|---------|--------|
| 2026-06-25 | 0.1.0 | Creación del documento metodológico CJ_OS Framework. |
| 2026-06-25 | 0.2.0 | Agregados Document Governance, Business Dictionary, Cognitive Model y KES-0 de Lenguaje Empresarial. |
