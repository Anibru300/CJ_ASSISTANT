# Document Governance — CJ_OS

**Versión:** 0.6.0  
**Fecha:** 2026-06-25  
**Estado:** Borrador inicial — pendiente de aprobación  
**Propósito:** Definir qué documentos son fuente oficial, quién los mantiene, cada cuándo se revisan y qué eventos obligan a actualizarlos.

---

## 1. Regla de arquitectura documental

> **Máximo 8–10 documentos maestros de conocimiento del negocio. Los documentos habilitadores (gobernanza, evidencia, canon, framework) son metodológicos y se mantienen separados.**

Si cada idea se convierte en documento maestro, el sistema documental se vuelve imposible de mantener. CJ_OS tendrá una arquitectura documental tan estricta como su arquitectura técnica.

---

## 2. Controlled Evolution (Evolución Controlada)

> **Durante las primeras sesiones KES, la arquitectura documental está en evolución controlada. Se permiten ajustes metodológicos mientras se aprende cómo opera realmente 3P.**

No se declara un `Architecture Freeze` antes de hablar con las personas que operan la empresa. Es muy probable que durante las primeras 3 o 4 sesiones se descubra que falta una pieza importante en la arquitectura.

### Fases de maduración documental

| Fase | Cuándo | Qué se permite |
|------|--------|----------------|
| **Diseño metodológico** | Hasta KES-Pilot | Crear y ajustar documentos metodológicos necesarios. |
| **Validación en terreno** | KES-Pilot, KES-0 y primeras 3 KES reales (Almacén, Compras, Ventas) | Evolución controlada. Las carencias se registran; solo se convierten en cambios metodológicos si se repiten o bloquean la captura. |
| **Architecture Freeze** | Después de validar Almacén, Compras, Ventas y Logística | Solo se refinan documentos existentes; nuevos documentos requieren justificación. |
| **Mantenimiento** | Post M2.8 | Cambios menores, actualizaciones por nuevos dominios o mejoras. |

> **Regla de cierre de diseño:** Durante las próximas tres KES (Almacén, Compras y Ventas) no se crean documentos nuevos, no se cambia la arquitectura, la ontología ni la gobernanza. Solo se registran problemas, vacíos, contradicciones y mejoras. Únicamente después de analizar esas tres sesiones se decidirá si realmente hace falta modificar la metodología.

### Criterio para crear un documento nuevo (después del freeze)

Solo se crea si cumple **las tres condiciones**:

1. **No cabe en ningún documento existente.**
2. **Será reutilizado por al menos tres dominios distintos.**
3. **Reduce complejidad, no la aumenta.**

Si falla una, no se crea. Se registra la necesidad en `Known Unknowns` o `Assumptions Register`.

---

## 3. Niveles de documentos

| Nivel | Descripción | Ejemplos |
|-------|-------------|----------|
| **Maestro** | Fuente oficial de verdad del negocio. Se modifica manualmente y con control. | Filosofía, Blueprint, Operating Model, Ontología, Business Dictionary, Event Catalog, Decision Catalog, Rules Catalog, Cognitive Model. |
| **Habilitador** | Documentos metodológicos que gobiernan cómo se maneja el conocimiento. | Document Governance, Knowledge Evidence Standard, Canon, Framework, Definition of Done. |
| **Derivado** | Se genera o actualiza a partir de documentos maestros. Puede ser vista, resumen o transformación. | Knowledge Graph, SYSTEM_MAP, Coverage Matrix, Traceability Matrix, reportes de auditoría. |
| **Temporal** | Borradores, notas de sesión, registros intermedios. Puede borrarse o archivarse. | Notas de KES, minutas, hipótesis pendientes, `Known Unknowns`, `Assumptions Register`. |

---

## 4. Documentos maestros oficiales

| Documento | Propietario | Puede modificar | Revisión mínima | Evento de actualización | Depende de |
|-----------|-------------|-----------------|-----------------|--------------------------|------------|
| `CJ_OS_PHILOSOPHY.md` | Carlos | Carlos | Trimestral | Cambio de valores, autonomía o riesgos éticos. | — |
| `CJ_OS_BLUEPRINT.md` | ChatGPT / Arquitecto | ChatGPT, con aprobación de Carlos | Trimestral | Cambio de dominios, tecnología o arquitectura. | Filosofía |
| `CJ_OS_OPERATING_MODEL.md` | Carlos + Líderes de área | Knowledge Engineer, con validación de área | Mensual durante KES | Cada KES completada. | Blueprint, Business Dictionary |
| `CJ_OS_BUSINESS_DICTIONARY.md` | Carlos | Knowledge Engineer, con validación de área | Cada KES | Descubrimiento de nuevo término o cambio de significado. | Operating Model |
| `CJ_OS_ONTOLOGY.md` | ChatGPT / Arquitecto | Knowledge Engineer, con validación técnica y de negocio | Cada KES | Nuevo objeto, atributo o relación validada. | Operating Model, Business Dictionary |
| `CJ_OS_EVENT_CATALOG.md` | ChatGPT / Arquitecto | Knowledge Engineer | Cada KES | Nuevo evento de negocio identificado. | Operating Model, Ontología |
| `CJ_OS_DECISION_CATALOG.md` | Carlos + Líderes de área | Knowledge Engineer | Cada KES | Nueva decisión o cambio de responsable/autonomía. | Operating Model, Rules Catalog |
| `CJ_OS_RULES_CATALOG.md` | Carlos + Líderes de área | Knowledge Engineer | Cada KES | Nueva regla o cambio de prioridad/criticalidad. | Operating Model, Decision Catalog |
| `CJ_OS_COGNITIVE_MODEL.md` | ChatGPT / Arquitecto | ChatGPT, con aprobación de Carlos | Trimestral | Cambio en modelo de decisión, autonomía o resolución de conflictos. | Filosofía, Rules Catalog, Decision Catalog |
| `CJ_OS_FRAMEWORK.md` | ChatGPT / Arquitecto | ChatGPT, con aprobación de Carlos | Semestral | Mejora metodológica del framework. | Todos los maestros |
| `CJ_OS_KNOWLEDGE_EVIDENCE_STANDARD.md` | ChatGPT / Arquitecto | ChatGPT, con aprobación de Carlos | Trimestral | Nuevo tipo de evidencia o ajuste de confianza. | KAP, Cognitive Model |
| `CJ_OS_CANON.md` | ChatGPT / Arquitecto | ChatGPT, con aprobación de Carlos | Trimestral | Cambio en documentos canónicos o jerarquía. | Todos los maestros y habilitadores |
| `CJ_OS_DEFINITION_OF_DONE.md` | ChatGPT / Arquitecto | ChatGPT, con aprobación de Carlos | Trimestral | Nuevo criterio de terminado. | Todos los maestros y habilitadores |

> **Total de maestros de negocio: 10.** Límite máximo vigilado.
> **Total de habilitadores: 5.** Vigilar para no aumentar sin justificación.

---

## 5. Documentos derivados

| Documento | Generado/actualizado a partir de | Responsable | Frecuencia |
|-----------|----------------------------------|-------------|------------|
| `CJ_OS_KNOWLEDGE_GRAPH.md` | Operating Model + Ontología + Rules Catalog | Knowledge Engineer | Tras cada KES |
| `CJ_KNOWLEDGE_COVERAGE_MATRIX.md` | Registro de KES + maestros | Knowledge Engineer | Tras cada KES |
| `SYSTEM_MAP.md` | Blueprint + Operating Model | ChatGPT / Arquitecto | Trimestral |
| `docs/reports/*.md` | Maestros + sesiones | Knowledge Engineer | Bajo demanda |
| `docs/CJ_OS_CANON.md` | Document Governance + maestros | ChatGPT / Arquitecto | Cuando cambia un maestro |
| `docs/CJ_OS_TRACEABILITY_MATRIX.md` | Maestros + catálogos | Knowledge Engineer | Tras cada KES |
| `docs/archive/*.md` | Versiones obsoletas de maestros | Kimi / DevOps | Al deprecar |

---

## 6. Activos de conocimiento

Cada documento, catálogo, regla o término se administra como un **activo de conocimiento** con los siguientes atributos:

| Atributo | Descripción |
|----------|-------------|
| **Propietario** | Quién garantiza la validez del activo. |
| **Estado** | Descubierto / Documentado / Revisado / Validado / Implementado / Obsoleto. |
| **Cobertura** | Porcentaje del dominio cubierto. |
| **Evidencia** | Tipo y referencia de evidencia que respalda el activo. |
| **Fecha** | Última actualización o revisión. |
| **Responsable** | Quién mantiene el activo día a día. |
| **Dependencias** | Otros activos de los que depende. |

---

## 7. Arquitectura de la información

CJ_OS maneja tres niveles de información, cada uno en su lugar apropiado:

| Nivel | Tipo de información | Dónde vive | Ejemplos |
|-------|---------------------|------------|----------|
| **Nivel 1 — Conocimiento estratégico** | Reglas, políticas, ontología, decisiones, modelo cognitivo. | **Core** de CJ_OS (memoria semántica y motor de decisiones). | "Nunca existencia negativa", "No modificar vale cerrado". |
| **Nivel 2 — Conocimiento operativo** | Datos transaccionales del negocio. | **PostgreSQL** (base de datos estructurada). | Inventario, pedidos, compras, movimientos. |
| **Nivel 3 — Evidencia** | Documentos, archivos, comunicaciones, fotos, audios. | **Data Lake** (almacenamiento de archivos/binarios). | PDFs, fotos, Excel, correos, WhatsApp, manuales. |

> Esta separación permite que CJ_OS escale: el Core no se llena de archivos, la base de datos no almacena blobs pesados y el Data Lake conserva evidencia sin estructurar.

---

## 8. Documentos temporales

| Tipo | Ubicación | Vida útil |
|------|-----------|-----------|
| Notas de KES | `workspace/shared/kes_notes/` o `runtime/temp/` | Hasta aprobación oficial |
| Minutas | `docs/reports/` o `workspace/shared/minutes/` | 1 año o hasta consolidación |
| Hipótesis pendientes | `docs/reports/` marcadas como HIPÓTESIS | Hasta validación o descarte |
| Borradores de catálogos | Rama local o `runtime/temp/` | Hasta merge a maestro |
| Known Unknowns | `docs/reports/CJ_OS_KNOWN_UNKNOWNS.md` | Hasta cierre |
| Assumptions Register | `docs/reports/CJ_OS_ASSUMPTIONS_REGISTER.md` | Hasta validación o eliminación |

---

## 9. Flujo de cambio

```
Se detecta cambio
      ↓
¿Afecta un documento maestro?
      ↓ Sí
Actualizar maestro → Revisar → Aprobar
      ↓
Actualizar documentos derivados afectados
      ↓
Registrar cambio en CHANGELOG.md y DECISIONES.md
      ↓
Notificar propietarios de documentos dependientes
```

---

## 10. Rol de Kimi / DevOps durante la Evolución Controlada

Durante la Evolución Controlada, Kimi tiene dos responsabilidades:

1. **Constructor:** ajustar la metodología y los documentos según lo aprendido en cada KES.
2. **Auditor técnico:** detectar inconsistencias antes de que se consoliden.

Antes de cualquier cambio, Kimi debe preguntar:

- ¿Esto contradice otro documento?
- ¿Esto rompe una regla?
- ¿Esto cambia la ontología?
- ¿Esto modifica un evento?
- ¿Esto obliga a cambiar el modelo de datos?
- ¿Esto invalida una decisión anterior?

Si la respuesta es sí, no se avanza hasta resolver la inconsistencia o elevarla a Carlos.

### Regla de las próximas tres KES

Durante Almacén, Compras y Ventas:

- **No crear documentos nuevos.**
- **No cambiar arquitectura, ontología ni gobernanza.**
- **Solo registrar:** problemas, vacíos, contradicciones y mejoras.
- Después de las tres sesiones, analizar si alguna carencia realmente requiere un cambio metodológico.

Después del `Architecture Freeze`, el rol se vuelve predominantemente auditor.

### Instrucción prioritaria para Kimi

> A partir de este momento, el rol operativo de Kimi cambia oficialmente:
>
> **De constructor de la metodología a auditor y modelador del conocimiento.**
>
> Su trabajo ya no es producir documentos. Su trabajo es demostrar que el sistema de captura de conocimiento es **consistente, reutilizable y escalable**.
>
> Antes de proponer cualquier nuevo artefacto, Kimi debe demostrar que:
> 1. No es posible integrar esa información en los documentos actuales.
> 2. Resuelve un problema concreto detectado en una KES real.
> 3. Ahorra trabajo futuro.

---

## 11. Reglas de gobernanza

1. **Un concepto, un documento maestro.** Si un dato vive en dos maestros, se designa uno como fuente y el otro referencia.
2. **Todo cambio en maestro requiere aprobación de su propietario.**
3. **Los documentos derivados no se editan directamente para cambiar reglas de negocio.** Se edita el maestro y se regenera.
4. **Toda KES produce notas temporales que luego se consolidan en maestros.**
5. **El estado de cada ítem de conocimiento se mantiene en el maestro correspondiente.**
6. **Si un documento temporal tiene más de 30 días sin consolidarse, se archiva o elimina.**
7. **Todo documento debe pasar por estados Draft → Review → Validated → Baseline.**
8. **Un documento solo se marca `Baseline` cuando cumple su Definition of Done.**
9. **Cada nuevo documento debe ahorrar trabajo futuro. Si solo organiza mejor la información existente, no se crea.**
10. **Antes de proponer cualquier nuevo artefacto, Kimi debe demostrar que no es posible integrar esa información en los documentos actuales y explicar qué problema concreto resuelve.**

---

## 12. Matriz de dependencias

```
Filosofía
    ↓
Blueprint
    ↓
Business Dictionary
    ↓
Operating Model
    ↓
Ontología ← Operating Model
    ↓
Event Catalog ← Ontología
    ↓
Decision Catalog ← Operating Model
    ↓
Rules Catalog ← Decision Catalog
    ↓
Cognitive Model ← Rules Catalog + Decision Catalog + Filosofía
    ↓
Knowledge Graph ← Ontología + Operating Model + Rules Catalog
    ↓
Canon ← Todos los maestros
    ↓
Evidence Standard ← KAP + Cognitive Model
```

---

## Historial de cambios

| Fecha | Versión | Cambio |
|-------|---------|--------|
| 2026-06-25 | 0.1.0 | Creación de la gobernanza documental con clasificación maestro/derivado/temporal, propietarios, dependencias y reglas de cambio. |
| 2026-06-25 | 0.2.0 | Agregados documentos habilitadores (Canon, Evidence Standard), activos de conocimiento, arquitectura de tres niveles de información (Core / PostgreSQL / Data Lake). |
| 2026-06-25 | 0.3.0 | Agregado Architecture Freeze, criterios para descongelar, registros temporales Known Unknowns y Assumptions Register, y rol de Kimi como auditor técnico. |
| 2026-06-25 | 0.4.0 | Reemplazado Architecture Freeze por Controlled Evolution, agregados Definition of Done, Traceability Matrix, estados Baseline, reglas para nuevos documentos e instrucción prioritaria para Kimi. |
| 2026-06-25 | 0.5.0 | Cerrada fase de diseño: no más documentos metodológicos hasta 3 KES reales. Rol de Kimi oficializado como auditor y modelador del conocimiento. |
| 2026-06-25 | 0.6.0 | Agregado Knowledge Quality Score (KQS), ciclo de vida del conocimiento extendido, separación observación/patrón/práctica/regla, pregunta de sabiduría y regla estricta de no cambios metodológicos durante las próximas 3 KES. |
