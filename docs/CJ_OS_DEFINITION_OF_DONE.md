# Definition of Done (DoD) — CJ_OS

**Versión:** 0.1.0  
**Fecha:** 2026-06-25  
**Estado:** Habilitador — en revisión bajo Controlled Evolution  
**Propósito:** Definir cuándo un documento o activo de conocimiento se considera realmente terminado y puede marcarse como baseline.

---

## 1. Principio fundamental

> **Un documento no está terminado porque tenga muchas páginas. Está terminado cuando puede ser usado sin generar dudas ni inconsistencias.**

El DoD aplica a todos los documentos maestros, habilitadores y derivados de CJ_OS.

---

## 2. Estados de madurez de un documento

| Estado | Significado | ¿Puede usarse para decisiones? |
|--------|-------------|--------------------------------|
| **Draft** | Borrador en construcción. | No |
| **Review** | En revisión por propietario o pares. | Solo con advertencia. |
| **Validated** | Aprobado por propietario y responsable de dominio. | Sí |
| **Baseline** | Versión oficial congelada; cambios requieren justificación. | Sí |
| **Deprecated** | Obsoleto; reemplazado por otra versión o documento. | No |

> **Ningún documento en estado `Draft` o `Review` alimenta el modelo de datos, APIs, workflows o decisiones automáticas.**

---

## 3. Definition of Done por documento

### `CJ_OS_PHILOSOPHY.md`

- [ ] Misión, valores y Constitución redactados.
- [ ] Niveles de autonomía A0-A5 definidos.
- [ ] Modelo de aprendizaje supervisado descrito.
- [ ] No contradice al Blueprint ni al Cognitive Model.
- [ ] Validado por Carlos.

### `CJ_OS_BLUEPRINT.md`

- [ ] No contradice ningún otro documento.
- [ ] Los 9 dominios operativos y 2 habilitadores están definidos.
- [ ] Todos los conceptos existen en la Ontología o en el Business Dictionary.
- [ ] No existen `Known Unknowns` críticos sin resolver relacionados con la arquitectura.
- [ ] Validado por Carlos.

### `CJ_OS_OPERATING_MODEL.md`

- [ ] Todos los procesos AS-IS documentados.
- [ ] Todos los procesos revisados con el responsable del dominio.
- [ ] Excepciones principales documentadas.
- [ ] Reglas críticas identificadas y vinculadas al Rules Catalog.
- [ ] Decisiones clave con responsable y nivel de autonomía.
- [ ] KPIs definidos con metas.
- [ ] Nivel de confianza promedio > 95%.
- [ ] Validado por Carlos y líderes de área.

### `CJ_OS_BUSINESS_DICTIONARY.md`

- [ ] Términos transversales definidos.
- [ ] Cada término tiene sinónimos aceptados y lo que NO significa.
- [ ] Cada término tiene propietario asignado.
- [ ] No hay términos ambiguos entre dominios.
- [ ] Validado en KES-0.

### `CJ_OS_ONTOLOGY.md`

- [ ] Ningún objeto sin atributos.
- [ ] Ningún atributo sin tipo, propietario y dominio.
- [ ] Ningún evento referencia objetos inexistentes.
- [ ] Todas las relaciones son válidas y trazables.
- [ ] Restricciones de integridad definidas.
- [ ] Validado por ChatGPT / Arquitecto y responsables de dominio.

### `CJ_OS_EVENT_CATALOG.md`

Cada evento debe responder:

- [ ] ¿Quién lo genera?
- [ ] ¿Qué lo dispara?
- [ ] ¿Qué datos lleva?
- [ ] ¿Quién lo consume?
- [ ] ¿Qué decisiones puede provocar?

Además:

- [ ] Nomenclatura `sustantivo_verbo` consistente.
- [ ] Payload definido.
- [ ] Eventos críticos vinculados a reglas.

### `CJ_OS_DECISION_CATALOG.md`

- [ ] Cada decisión tiene información necesaria.
- [ ] Cada decisión tiene opciones y resultados posibles.
- [ ] Responsable asignado.
- [ ] Nivel de autonomía A0-A5 definido.
- [ ] Vinculado a eventos y reglas relacionadas.

### `CJ_OS_RULES_CATALOG.md`

- [ ] Cada regla tiene enunciado claro.
- [ ] Cada regla tiene tipo (integridad, autorización, flujo, excepción).
- [ ] Cada regla tiene criticalidad.
- [ ] Cada regla tiene evidencia que la respalda.
- [ ] Evento relacionado identificado.
- [ ] Definido quién puede romperla y bajo qué condiciones.

### `CJ_OS_KNOWLEDGE_GRAPH.md`

- [ ] Todas las tripletas provienen de documentos validados.
- [ ] No hay relaciones contradictorias.
- [ ] Cada relación es trazable a Ontología, Operating Model o Rules Catalog.

### `CJ_OS_COGNITIVE_MODEL.md`

- [ ] Ciclo de decisión definido.
- [ ] Niveles de autonomía A0-A5 descritos.
- [ ] Modelo de incertidumbre definido.
- [ ] Resolución de conflictos entre reglas documentada.
- [ ] Validado por Carlos.

### `CJ_OS_CANON.md`

- [ ] Lista de documentos canónicos completa.
- [ ] Jerarquía de resolución de conflictos definida.
- [ ] Reglas del Canon validadas.

### `CJ_OS_DOCUMENT_GOVERNANCE.md`

- [ ] Niveles de documentos definidos.
- [ ] Propietarios y responsables asignados.
- [ ] Flujo de cambio documentado.
- [ ] Controlled Evolution y criterios de freeze claros.

### `CJ_OS_KNOWLEDGE_EVIDENCE_STANDARD.md`

- [ ] Tipos de evidencia definidos.
- [ ] Niveles de confianza asignados.
- [ ] Plantilla de registro de evidencia disponible.
- [ ] Relación con Cognitive Model establecida.

### `CJ_OS_FRAMEWORK.md`

- [ ] Flujo metodológico completo.
- [ ] Descripción de cada capa.
- [ ] Criterios de madurez del framework.
- [ ] Concepto de Knowledge Pack documentado.

### `CJ_OS_KNOWLEDGE_ACQUISITION_PROTOCOL.md`

- [ ] Fases de sesión definidas.
- [ ] Metadatos de conocimiento completos.
- [ ] Tipos de sesión KES-D/I/O/V descritos.
- [ ] Métricas de éxito definidas.
- [ ] KES-Pilot incluido.

---

## 4. Definition of Done de un ítem de conocimiento

Cada hecho, regla, heurística o excepción debe cumplir:

- [ ] Enunciado claro en una oración.
- [ ] Clasificación por tipo, capa, naturaleza y estabilidad.
- [ ] Criticalidad asignada.
- [ ] Fuente y evidencia documentadas.
- [ ] Estado `Validado` o `Implementado`.
- [ ] Sin contradicciones con otros ítems validados.
- [ ] Trazable en la Traceability Matrix.

---

## 5. Reglas generales del DoD

1. **Ningún documento pasa a `Validated` sin cumplir su DoD específico.**
2. **Ningún documento pasa a `Baseline` sin estar `Validated`.**
3. **Cualquier cambio a un documento `Baseline` requiere justificación y revisión de impacto.**
4. **Si un documento no responde una pregunta concreta, no debería existir.**
5. **Cada nuevo documento debe ahorrar trabajo futuro. Si solo reorganiza información existente, no se crea.**

---

## Historial de cambios

| Fecha | Versión | Cambio |
|-------|---------|--------|
| 2026-06-25 | 0.1.0 | Creación del Definition of Done con estados de madurez, DoD por documento y reglas generales. |
