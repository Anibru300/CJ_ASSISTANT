# CJ_OS Canon

**Versión:** 0.1.0  
**Fecha:** 2026-06-25  
**Estado:** Documento maestro — pendiente de aprobación  
**Propósito:** Definir qué documentos son la verdad oficial de CJ_OS. Cuando haya dudas o inconsistencias, este Canon resuelve cuál documento manda.

---

## 1. Principio fundamental

> **El Canon no es conocimiento del negocio. Es el mapa de dónde vive el conocimiento oficial.**

Si dos documentos dicen cosas distintas, el Canon indica cuál es la fuente de verdad. Todo lo demás es derivado, temporal o de referencia.

---

## 2. Documentos canónicos (fuente oficial)

| Documento | Código | ¿Es fuente oficial? | Propietario | ¿Sobre qué manda? |
|-----------|--------|---------------------|-------------|-------------------|
| `CJ_OS_PHILOSOPHY.md` | PHIL | ✅ Sí | Carlos | Valores, misión, autonomía, Constitución. |
| `CJ_OS_BLUEPRINT.md` | BLUE | ✅ Sí | ChatGPT / Arquitecto | Arquitectura, dominios, componentes, tecnología. |
| `CJ_OS_OPERATING_MODEL.md` | OPMO | ✅ Sí | Carlos + Líderes de área | Procesos, actores, objetos, reglas, decisiones, KPIs por dominio. |
| `CJ_OS_BUSINESS_DICTIONARY.md` | DICT | ✅ Sí | Carlos + Líderes de área | Significado oficial de cada término. |
| `CJ_OS_ONTOLOGY.md` | ONTO | ✅ Sí | ChatGPT / Arquitecto | Entidades, atributos, relaciones y restricciones. |
| `CJ_OS_EVENT_CATALOG.md` | EVCT | ✅ Sí | ChatGPT / Arquitecto | Eventos de negocio, payload, generadores y consumidores. |
| `CJ_OS_DECISION_CATALOG.md` | DCCT | ✅ Sí | Carlos + Líderes de área | Decisiones, opciones, información necesaria, responsable, autonomía. |
| `CJ_OS_RULES_CATALOG.md` | RLCT | ✅ Sí | Carlos + Líderes de área | Reglas de negocio, prioridad, criticalidad, excepciones. |
| `CJ_OS_COGNITIVE_MODEL.md` | COGM | ✅ Sí | ChatGPT / Arquitecto | Cómo decide, pregunta, ejecuta, propone y escala CJ_OS. |
| `CJ_OS_DOCUMENT_GOVERNANCE.md` | GOVN | ✅ Sí | ChatGPT / Arquitecto | Reglas de documentos maestros, derivados y temporales. |
| `CJ_OS_KNOWLEDGE_EVIDENCE_STANDARD.md` | KESV | ✅ Sí | ChatGPT / Arquitecto | Qué evidencia respalda cada conocimiento y cuánto confiar. |
| `CJ_OS_FRAMEWORK.md` | FWRK | ✅ Sí | ChatGPT / Arquitecto | Metodología reutilizable de implementación. |
| `CJ_OS_CANON.md` | CANN | ✅ Sí | ChatGPT / Arquitecto | Este documento: qué documentos son oficiales. |

> **Total de documentos canónicos: 13.** El límite de 8–10 de Document Governance aplica a documentos de **conocimiento del negocio**; los documentos metodológicos (GOVN, KESV, FWRK, CANN) se consideran habilitadores.

---

## 3. Documentos derivados (no son fuente, se regeneran)

| Documento | Generado a partir de | Responsable |
|-----------|----------------------|-------------|
| `CJ_OS_KNOWLEDGE_GRAPH.md` | OPMO + ONTO + RLCT | Knowledge Engineer |
| `CJ_KNOWLEDGE_COVERAGE_MATRIX.md` | Registro de KES + maestros | Knowledge Engineer |
| `SYSTEM_MAP.md` | BLUE + OPMO | Arquitecto |
| `docs/reports/*.md` | Maestros + sesiones | Knowledge Engineer / Auditor |
| `docs/archive/*.md` | Versiones obsoletas de maestros | DevOps |

---

## 4. Jerarquía de resolución de conflictos

Si dos documentos se contradicen, se resuelve en este orden:

1. **Canon** (`CJ_OS_CANON.md`) — decide cuál documento manda.
2. **Filosofía** (`CJ_OS_PHILOSOPHY.md`) — valores y límites éticos.
3. **Blueprint** (`CJ_OS_BLUEPRINT.md`) — arquitectura y dominios.
4. **Business Dictionary** (`CJ_OS_BUSINESS_DICTIONARY.md`) — significado de términos.
5. **Operating Model** (`CJ_OS_OPERATING_MODEL.md`) — procesos y reglas del negocio.
6. **Rules Catalog** (`CJ_OS_RULES_CATALOG.md`) — reglas específicas.
7. **Decision Catalog** (`CJ_OS_DECISION_CATALOG.md`) — decisiones y responsables.
8. **Ontología** (`CJ_OS_ONTOLOGY.md`) — entidades y relaciones.
9. **Event Catalog** (`CJ_OS_EVENT_CATALOG.md`) — eventos.
10. **Cognitive Model** (`CJ_OS_COGNITIVE_MODEL.md`) — cómo actúa CJ_OS ante la ambigüedad.

> **Ejemplo:** Si el Operating Model dice "un vale se puede modificar" y el Rules Catalog dice "nunca modificar un vale cerrado", gana el Rules Catalog porque es más específico. Si persiste el conflicto, se escala a Carlos.

---

## 5. Reglas del Canon

1. **Un concepto solo puede tener una fuente oficial.**
2. **Los documentos derivados no pueden contradecir a los canónicos.**
3. **Todo cambio en un documento canónico debe reflejarse en sus derivados dependientes.**
4. **Si un documento canónico queda obsoleto, el Canon se actualiza primero.**
5. **Cualquier duda sobre cuál documento manda se resuelve consultando este Canon.**

---

## 6. Relación con activos de conocimiento

Cada documento canónico es un **activo de conocimiento** con:

- **Propietario**
- **Estado**
- **Cobertura**
- **Evidencia**
- **Fecha de última revisión**
- **Responsable de mantenimiento**
- **Dependencias**

---

## Historial de cambios

| Fecha | Versión | Cambio |
|-------|---------|--------|
| 2026-06-25 | 0.1.0 | Creación del Canon con lista de documentos canónicos, derivados, jerarquía de resolución de conflictos y reglas. |
