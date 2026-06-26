# Knowledge Acquisition Protocol (KAP) — CJ_OS

**Versión:** 0.7.0  
**Fecha:** 2026-06-25  
**Estado:** Protocolo maestro — pendiente de validación por Carlos  
**Propósito:** Definir exactamente cómo se realiza una Knowledge Engineering Session (KES) / Sesión de Ingeniería del Conocimiento (SIC) para que cualquier persona pueda ejecutarla con la misma calidad.

---

## 1. Principio fundamental

> **Las KES no son solo sesiones de extracción. Son sesiones de descubrimiento.**
>
> El experto muchas veces no sabe que sabe. Las mejores reglas aparecen durante la conversación o al observar el trabajo real, no en la primera respuesta.

Cada sesión produce conocimiento estructurado, trazable, medible y con nivel de confianza. Una sola conversación bien conducida alimenta automáticamente:

- Business Dictionary
- Operating Model
- Ontología Empresarial
- Knowledge Graph
- Catálogo de Eventos
- Catálogo de Decisiones
- Catálogo de Reglas
- Cognitive Model
- Knowledge Coverage Matrix
- Registro de fuentes y confianza

> **Antes de cualquier KES de dominio, se realiza la KES-0: Sesión de Lenguaje Empresarial.**
> Esta sesión define el vocabulario oficial de 3P en el `CJ_OS_BUSINESS_DICTIONARY.md`.

---

## 2. Tipos de conocimiento

Cada pieza de conocimiento capturada debe clasificarse en uno de cuatro tipos:

| Tipo | Definición | Ejemplo | Confianza típica |
|------|------------|---------|------------------|
| **Hecho** | Dato observable y verificable. | "El rack A-05 tiene capacidad para 40 cajas." | Alta (90-100%) |
| **Regla** | Restricción o comportamiento obligatorio. | "Nunca modificar un vale cerrado." | Alta (90-100%) |
| **Heurística** | Experiencia práctica, no es regla formal. | "Si llega mercancía un viernes, es mejor revisarla el mismo día." | Media (50-80%) |
| **Excepción** | Qué hacer cuando algo falla o no sigue el flujo normal. | "Cuando SAE falla, primero se captura en Excel." | Media-Alta (60-90%) |

> **La IA necesita especialmente heurísticas y excepciones.** Es el conocimiento que nunca aparece en los procedimientos formales.

> **Conocimiento vs. Sabiduría:** No todo lo que capturen debe convertirse en regla. Una observación puede convertirse en patrón, luego en buena práctica y solo después de validación suficiente en regla aprobada.

### 2.1 Madurez del conocimiento

Cada ítem de conocimiento puede estar en uno de estos niveles de madurez:

| Madurez | Descripción | Ejemplo | ¿Regla? |
|---------|-------------|---------|---------|
| **Observación** | Algo que se notó una o pocas veces. | "Francisco revisa dos veces los productos del proveedor X." | No |
| **Patrón** | Se repite con frecuencia. | "Siempre que llega del proveedor X, hay discrepancias." | No |
| **Buena práctica** | Recomendación probada, pero no obligatoria. | "Revisar dos veces los productos del proveedor X." | No |
| **Regla aprobada** | Comportamiento obligatorio validado. | "Todo producto del proveedor X requiere doble revisión." | Sí |

> **No se institucionalizan costumbres demasiado pronto.** Una observación solo se convierte en regla después de evidencia y aprobación.

### 2.2 Naturaleza del conocimiento

No todo el conocimiento vale lo mismo. Cada pieza se clasifica también por su alcance:

| Naturaleza | Descripción | Ejemplo | Criticalidad típica |
|------------|-------------|---------|---------------------|
| **Universal** | Aplica a cualquier empresa, independiente de 3P. | Qué es un inventario, FIFO, trazabilidad, ISO 9001. | Media |
| **Específico de 3P** | Depende de cómo opera esta empresa. | Francisco hace esto primero, usamos SAE, este formato. | Alta |
| **Estratégico** | Explica por qué se trabaja así. Es el conocimiento del gerente experimentado. | "Nunca compramos menos de X porque el envío es caro", "Ese cliente siempre tiene prioridad". | Muy alta |

> **El conocimiento estratégico raramente aparece en procedimientos, pero es lo que diferencia a un buen operador de un sistema que solo sigue reglas.**

### 2.3 Capas de conocimiento

Además del tipo, cada conocimiento pertenece a una capa según su velocidad de cambio:

| Capa | Descripción | Ejemplos | Dónde vive |
|------|-------------|----------|------------|
| **Permanente** | Cómo funciona la empresa. Cambia poco. | Qué es un vale, qué es un rack. | Business Dictionary, Ontología, Operating Model. |
| **Operativo** | Lo que cambia constantemente. | Existencias, pedidos, compras del día. | Base de datos, eventos, memoria operativa. |
| **Estratégico** | Cómo mejorar. | Detectar productos sin movimiento, reducir mermas. | Cognitive Model, reportes, recomendaciones de IA. |

### 2.4 Estabilidad del conocimiento

Además del tipo y la capa, cada conocimiento tiene una estabilidad que indica con qué frecuencia debe revisarse:

| Estabilidad | Descripción | Ejemplo | Revisión sugerida |
|-------------|-------------|---------|-------------------|
| **Estable** | Casi nunca cambia. | Qué es un vale, qué es un SKU. | Anual |
| **Variable** | Cambia con cierta frecuencia. | Stock mínimo/máximo, listas de proveedores. | Trimestral |
| **Temporal** | Solo aplica en un periodo o situación. | Promoción, contingencia por falla de sistema. | Al vencer el periodo |
| **Experimental** | Se está probando. | Nueva política de surtido, nuevo umbral de merma. | Mensual |

> **CJ_OS debe memorizar el conocimiento estable casi para siempre y revisar constantemente el experimental.**

---

## 3. Ciclo de vida del conocimiento

Cada ítem de conocimiento atraviesa un ciclo completo:

```text
Descubierto
    ↓
Documentado
    ↓
Validado
    ↓
Usado
    ↓
Medido
    ↓
Mejorado
    ↓
Obsoleto
```

| Estado | Significado | ¿Cuenta para cobertura? |
|--------|-------------|-------------------------|
| **Descubierto** | Alguien lo mencionó en una sesión. | No |
| **Documentado** | Ya quedó escrito en notas temporales. | No |
| **Revisado** | Se comparó con la realidad u otras fuentes. | No |
| **Validado** | El responsable del área lo aprobó. | **Sí** |
| **Usado** | CJ_OS lo utiliza en decisiones o recomendaciones. | **Sí** |
| **Medido** | Se ha evaluado si sigue siendo correcto en operación. | **Sí** |
| **Mejorado** | Se refinó con base en mediciones. | **Sí** |
| **Obsoleto** | Ya no aplica. | No |

> **Solo los ítems Validado, Usado, Medido o Mejorado suman a la cobertura oficial.**
> El ciclo de vida asegura que el conocimiento no solo se capture, sino que evolucione con el tiempo.

---

## 4. Criticalidad del conocimiento

Cada regla o conocimiento debe tener un nivel de criticalidad. Esto permite a CJ_OS resolver conflictos y priorizar:

| Nivel | Significado | Ejemplo |
|-------|-------------|---------|
| **Crítica** | No puede violarse nunca. Afecta integridad, dinero o legalidad. | Nunca existencia negativa. No modificar vale cerrado. |
| **Alta** | Debe cumplirse salvo autorización explícita. | Fotografiar mercancía dañada. |
| **Media** | Recomendación fuerte, pero puede ignorarse con justificación. | Notificar cuando un rack llega al 80%. |
| **Baja** | Buena práctica, flexible. | Orden sugerido de acomodo. |

---

## 5. Metadatos de cada pieza de conocimiento

Cada hecho, regla, heurística o excepción debe llevar:

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| **ID** | Código único. | `KES-01-ALM-REG-001` |
| **Dominio** | A qué área pertenece. | Almacén |
| **Categoría** | Actores, Objetos, Eventos, Procesos, Reglas, Excepciones, Decisiones, KPIs, Automatizaciones. | Reglas |
| **Tipo** | Hecho / Regla / Heurística / Excepción. | Regla |
| **Enunciado** | El conocimiento en una oración. | "Nunca modificar un vale cerrado." |
| **Fuente** | Quién lo dijo. | Francisco |
| **KES/SIC** | Código de la sesión. | KES-01 |
| **Fecha** | Cuándo se capturó. | 2026-06-25 |
| **Minuto** | Referencia aproximada de la sesión. | 18:32 |
| **Participantes** | Quiénes estaban presentes. | Carlos, Salvador, Francisco |
| **Estado** | Descubierto / Documentado / Revisado / Validado / Usado / Medido / Mejorado / Obsoleto. | Validado |
| **Validado por** | Quién confirmó que es cierto. | Carlos |
| **Confianza** | Porcentaje del 0% al 100%. | 100% |
| **Criticalidad** | Crítica / Alta / Media / Baja. | Crítica |
| **Capa** | Permanente / Operativo / Estratégico. | Permanente |
| **Naturaleza** | Universal / Específico de 3P / Estratégico. | Específico de 3P |
| **Estabilidad** | Estable / Variable / Temporal / Experimental. | Estable |
| **Evidencia** | Tipo de evidencia que respalda el conocimiento. | Procedimiento oficial |
| **Referencia de evidencia** | Dónde encontrar la evidencia. | `procedimientos/almacen/recepcion_v1.2.pdf` |
| **Confianza de evidencia** | Confianza asociada al tipo de evidencia. | 100% |
| **Madurez** | Observación / Patrón / Buena práctica / Regla aprobada. | Regla aprobada |
| **KQS** | Knowledge Quality Score (0–100). | 95 |
| **Recolectada en** | Tipo y sesión de recolección. | KES-D-01-ALM |
| **Responsable de evidencia** | Quién puede entregar o confirmar la evidencia. | Salvador |
| **Depende de** | Otros conocimientos relacionados. | `KES-01-ALM-OBJ-005` (Vale) |

---

## 5.1 Knowledge Quality Score (KQS)

Cada ítem de conocimiento recibe una puntuación de calidad. No se mide cantidad ni cobertura; se mide **calidad**.

### Criterios y pesos

| Criterio | Peso | ¿Qué evalúa? |
|----------|------|--------------|
| **Tiene evidencia** | 20% | ¿Hay una fuente objetiva que lo respalde? |
| **Validado por responsable** | 20% | ¿El propietario del dominio lo aprobó? |
| **No contradice otro conocimiento** | 15% | ¿Es consistente con reglas, decisiones y eventos existentes? |
| **Tiene trazabilidad** | 15% | ¿Se sabe de dónde viene y quién lo usa? |
| **Es accionable** | 15% | ¿CJ_OS puede usarlo para decidir, proponer o ejecutar? |
| **Tiene contexto suficiente** | 15% | ¿Se entiende cuándo aplica, por qué y bajo qué condiciones? |

### Niveles de calidad

| Puntaje | Nivel | Uso en CJ_OS |
|---------|-------|--------------|
| **95–100** | Excelente | Puede usarse para automatización y decisiones autónomas. |
| **85–94** | Bueno | Usar con supervisión ligera. |
| **70–84** | Revisar | Requiere validación adicional antes de automatizar. |
| **< 70** | No utilizar | Solo informar o marcar como hipótesis. |

> **CJ_OS solo usará con confianza el conocimiento con KQS ≥ 85.**

---

## 5.2 Activos de conocimiento

Cada documento o pieza de conocimiento de CJ_OS se trata como un **activo de conocimiento**.

| Atributo | Descripción |
|----------|-------------|
| **Propietario** | Quién garantiza que el activo es correcto y vigente. |
| **Estado** | Descubierto / Documentado / Revisado / Validado / Usado / Medido / Mejorado / Obsoleto. |
| **Cobertura** | Porcentaje del dominio que cubre. |
| **Evidencia** | Tipo y referencia de evidencia que respalda el activo. |
| **Fecha** | Última actualización o revisión. |
| **Responsable** | Quién mantiene el activo día a día. |
| **Dependencias** | Otros activos de los cuales depende. |

> **CJ_OS no administra documentos. Administra activos de conocimiento.**

---

## 6. Protocolo paso a paso de una KES

### Fase Piloto — KES-Pilot: Demostrar que la metodología funciona

La KES-Pilot no busca documentar todo un dominio. Busca **probar que la metodología puede modelar un proceso real**.

#### Proceso sugerido para la pilot

**Entrada de mercancía de proveedor** (Almacén).

#### Durante la sesión se intenta llenar

- Operating Model (AS-IS del proceso).
- Ontología (objetos y atributos involucrados).
- Business Dictionary (términos usados).
- Event Catalog (eventos generados).
- Decision Catalog (decisiones del proceso).
- Rules Catalog (reglas críticas).
- Knowledge Graph (relaciones).
- Evidencias (tipo y referencia).
- Known Unknowns.
- Assumptions Register.

#### Criterio de éxito de la pilot

Al finalizar se hace una revisión honesta:

> **¿Hubo información que no supimos dónde colocar?**

- **Sí:** la metodología necesita ajustes antes de KES-0.
- **No:** la metodología pasó la prueba y puede usarse en sesiones oficiales.

**Segundo criterio de éxito:**

> Una persona que nunca ha trabajado en 3P debe poder leer la documentación generada y entender exactamente cómo funciona el proceso, por qué se hace así y qué decisiones tomaría un empleado experimentado en situaciones normales y excepcionales.

#### Objetivos adicionales

1. Validar que las preguntas generan información útil.
2. Medir cuánto tarda documentar un proceso.
3. Detectar qué partes del protocolo sobran o faltan.
4. Ajustar la metodología una sola vez antes de las sesiones oficiales.

> Sin KES-Pilot aprobada, no inicia KES-0.

### Fase 0 — KES-0: Lenguaje Empresarial (previo a cualquier KES de dominio)

Antes de la KES-1 de Almacén, se realiza una sesión con Carlos y los líderes de área para **construir el lenguaje oficial de 3P**.

Objetivos de KES-0:

1. Definir términos transversales: vale, solicitud, pedido, orden de compra, entrada, recepción, surtido, embarque, existencia, stock.
2. Registrar sinónimos aceptados y lo que NO significa cada término.
3. Asignar propietario del término.
4. Validar el `CJ_OS_BUSINESS_DICTIONARY.md`.

> El resultado de KES-0 no es solo un diccionario. Es un **lenguaje corporativo estándar** que usarán CJ_OS, el SGC, capacitaciones, reportes, dashboards, workflows de n8n, tablas de PostgreSQL y prompts de IA.
>
> Sin KES-0 aprobada, no inicia ninguna KES de dominio.

### Fase 1 — Preparación

1. **Definir el dominio.** ¿Qué área se va a trabajar? (ej. Almacén).
2. **Identificar al experto.** ¿Quién conoce mejor el área? (ej. Salvador y Francisco).
3. **Confirmar objetivo.** ¿Qué se espera lograr en la sesión?
4. **Revisar cobertura previa y Business Dictionary.** ¿Hay conocimiento de este dominio ya capturado? ¿Los términos están definidos?
5. **Preparar plantilla.** Abrir ficha maestra del dominio y matriz de cobertura.
6. **Preparar espacio de notas temporales.** Crear archivo temporal de la sesión (`workspace/shared/kes_notes/KES-01-ALM-notas.md`).
7. **Identificar evidencias disponibles.** Procedimientos, formatos, SAE, Excel, manuales, políticas.

### Fase 2 — Extracción (solo notas temporales)

Una sesión de dominio puede combinarse con varios tipos de recolección:

| Tipo | Nombre | Objetivo |
|------|--------|----------|
| **KES-D** | Documental | Revisar procedimientos, formatos, SAE, Excel, políticas. |
| **KES-I** | Entrevista | Entrevistar a responsables y operadores. |
| **KES-O** | Observación | Ver trabajar al área en condiciones reales. |
| **KES-V** | Validación | Presentar el conocimiento capturado al experto para confirmar o corregir. |

> **Durante la extracción NO se tocan documentos maestros.** Solo se llenan notas temporales.

1. **Objetivo del dominio.** ¿Para qué existe esta área?
2. **Actores.** ¿Quién participa?
3. **Objetos.** ¿Qué entidades existen?
4. **Eventos.** ¿Qué cosas pueden ocurrir?
5. **Procesos.** Cada proceso responde 5 preguntas:
    - ¿Qué lo inicia?
    - ¿Qué lo termina?
    - ¿Qué información consume?
    - ¿Qué información produce?
    - ¿Qué evento genera?
6. **Reglas.** ¿Qué nunca debe violarse?
7. **Excepciones.** ¿Qué pasa cuando algo falla?
8. **Decisiones.** ¿Qué decisiones se toman y quién las autoriza?
9. **KPIs.** ¿Cómo se mide el desempeño?
10. **Automatizaciones futuras.** ¿Qué podría hacer CJ_OS?
11. **Heurísticas.** ¿Qué experiencia práctica no está escrita?
12. **Pregunta final:** *¿Qué haría el mejor gerente de esta área que hoy nadie hace?*
13. **Pregunta de sabiduría obligatoria por proceso:** *"Si mañana contrataras a un nuevo gerente, ¿qué le explicarías que no aparece en ningún procedimiento?"*

> **Durante la extracción NO se tocan documentos maestros.** Solo se llenan notas temporales.

### Fase 3 — Revisión

18. **Depurar notas temporales.** Eliminar duplicados, corregir malentendidos, completar ambigüedades.
19. **Clasificar cada pieza.** ¿Es hecho, regla, heurística o excepción?
20. **Asignar capa.** ¿Permanente, operativo o estratégico?
21. **Asignar criticalidad.** ¿Crítica, alta, media o baja?
22. **Asignar estado inicial.** Descubierto → Documentado → Revisado.
23. **Asignar evidencia.** Tipo, referencia, confianza base y responsable de evidencia.
24. **Actualizar Known Unknowns.** Registrar preguntas sin respuesta y su vía de cierre.
25. **Actualizar Assumptions Register.** Registrar suposiciones sin validar.
26. **Resolver dudas con el experto.** Si hay ambigüedad, se pregunta antes de validar.

### Fase 4 — Aprobación

27. **Enviar notas revisadas al propietario del dominio.**
28. **El propietario valida o rechaza cada ítem.**
29. **Los ítems aprobados cambian a estado Validado.**
30. **Los ítems rechazados se marcan como Hipótesis u Obsoleto.**
31. **Carlos aprueba conocimiento crítico.**

### Fase 5 — Consolidación en documentos oficiales

32. **Actualizar documentos maestros.** Business Dictionary, Ontología, Operating Model, catálogos, Cognitive Model.
33. **Actualizar documentos derivados.** Knowledge Graph, Coverage Matrix.
34. **Actualizar registro de fuentes y evidencias.**
35. **Decidir si la sesión termina.** Cobertura ≥ 90% en categorías críticas.

---

## 7. Criterios de cierre de una KES

Una KES se considera completa cuando:

- [ ] Objetivo del dominio validado.
- [ ] Actores identificados (cobertura 100%).
- [ ] Objetos identificados con atributos clave (cobertura ≥ 90%).
- [ ] Eventos principales identificados (cobertura ≥ 90%).
- [ ] Procesos principales documentados con 5 preguntas (cobertura ≥ 80%).
- [ ] Reglas críticas identificadas y validadas (cobertura ≥ 90%).
- [ ] Excepciones principales documentadas (cobertura ≥ 70%).
- [ ] Decisiones clave con responsable y autonomía (cobertura ≥ 80%).
- [ ] KPIs definidos (cobertura ≥ 70%).
- [ ] Automatizaciones futuras priorizadas.
- [ ] Pregunta final respondida.
- [ ] Conocimiento crítico validado por Carlos o responsable del dominio.

> **Si la cobertura no alcanza el umbral, la sesión continúa o se programa una sesión complementaria.**

### 7.1 Métricas de éxito de una KES

El éxito de una sesión no se mide por documentos producidos, sino por calidad del conocimiento capturado:

| Métrica | Objetivo |
|---------|----------|
| Procesos reales capturados | 100% |
| Excepciones documentadas | > 95% |
| Reglas validadas | > 95% |
| Decisiones validadas | > 90% |
| Cobertura de conocimiento | > 90% |
| Contradicciones abiertas | < 5 |
| Conocimiento con evidencia | > 95% |
| Known Unknowns con vía de cierre | 100% de alta prioridad |
| Assumptions validadas o eliminadas | 100% de alto impacto |

### 7.2 Métricas de calidad del conocimiento

| Métrica | Descripción | Objetivo |
|---------|-------------|----------|
| **Densidad de conocimiento** | Cantidad de hechos, reglas, excepciones, decisiones, eventos y heurísticas capturados por unidad de tiempo. | Una sesión de 45 minutos debe producir decenas de ítems, no solo unos pocos. |
| **Reutilización** | Porcentaje del conocimiento de un dominio que sirve para otros dominios. | > 70% para considerar que la arquitectura es genérica y reutilizable. |

Ejemplo de densidad en una entrevista de 45 minutos:

```text
12 hechos
18 reglas
6 excepciones
9 decisiones
14 eventos
4 heurísticas
```

Si una sesión produce solo 3 reglas, algo está mal en el protocolo o en la preparación.

### 7.3 Revisión post-KES

Al finalizar cada sesión, responder obligatoriamente:

1. **¿Qué aprendimos que no sabíamos?**
2. **¿Qué supusimos y resultó falso?**
3. **¿Qué documento hubo que modificar?**
4. **¿Qué haríamos diferente en la siguiente sesión?**

> Estas respuestas hacen que la propia metodología evolucione de forma basada en evidencia.

---

## 8. Niveles de confianza

| Confianza | Significado | Uso en CJ_OS |
|-----------|-------------|--------------|
| **100%** | Validado por responsable y probado en operación. | Puede usarse para automatización A3. |
| **80-99%** | Validado, pero con poca historia operativa. | Usar con supervisión A2/A3. |
| **50-79%** | Hipótesis razonable, no validada formalmente. | Solo proponer (A1). |
| **<50%** | Dato anecdótico o no verificado. | Solo informar (A0) o solicitar validación. |

---

## 9. Identificadores de conocimiento

Cada pieza de conocimiento tendrá un ID codificado:

```text
KES-<numero_sesion>-<dominio>-<categoria>-<numero_correlativo>
```

Ejemplos:

- `KES-01-ALM-REG-001` → KES 1, Almacén, Regla, número 1.
- `KES-01-ALM-OBJ-005` → KES 1, Almacén, Objeto, número 5.
- `KES-01-ALM-HEU-003` → KES 1, Almacén, Heurística, número 3.
- `KES-01-ALM-EXC-002` → KES 1, Almacén, Excepción, número 2.

Códigos de dominio:

| Código | Dominio |
|--------|---------|
| LNG | Lenguaje Empresarial (KES-0) |
| DIR | Dirección |
| VEN | Ventas |
| COM | Compras |
| ALM | Almacén |
| LOG | Logística |
| CAL | Calidad |
| CON | Contabilidad |
| RRH | RRHH |
| IE | Inteligencia Empresarial |

Códigos de categoría:

| Código | Categoría |
|--------|-----------|
| OBJ | Objetos |
| ACT | Actores |
| EVT | Eventos |
| PRO | Procesos |
| REG | Reglas |
| HEU | Heurísticas |
| EXC | Excepciones |
| DEC | Decisiones |
| KPI | KPIs |
| AUT | Automatizaciones |
| TER | Términos (Business Dictionary) |

---

## 10. Registro de sesiones

Cada KES debe quedar registrada con:

| Campo | Valor |
|-------|-------|
| **Código** | KES-01 |
| **Dominio** | Almacén |
| **Fecha** | 2026-06-25 |
| **Duración** | 120 minutos |
| **Expertos** | Salvador, Francisco |
| **Knowledge Engineer** | Carlos / CJ_OS |
| **Objetivo** | Adquirir conocimiento operativo del almacén. |
| **Cobertura final** | Ver Knowledge Coverage Matrix. |
| **Pendientes** | Validar umbrales de merma, definir familias de producto. |
| **Estado** | COMPLETADA / INCOMPLETA / PENDIENTE |

---

## 11. Productos esperados de cada KES

Después de cada sesión deben actualizarse los maestros afectados:

1. `docs/CJ_OS_BUSINESS_DICTIONARY.md` (si emergen términos)
2. `docs/CJ_OS_OPERATING_MODEL.md`
3. `docs/CJ_OS_ONTOLOGY.md`
4. `docs/CJ_OS_EVENT_CATALOG.md`
5. `docs/CJ_OS_DECISION_CATALOG.md`
6. `docs/CJ_OS_RULES_CATALOG.md`
7. `docs/CJ_OS_COGNITIVE_MODEL.md` (si afecta decisiones o autonomía)

Y los derivados correspondientes:

8. `docs/CJ_OS_KNOWLEDGE_GRAPH.md`
9. `docs/CJ_KNOWLEDGE_COVERAGE_MATRIX.md`
10. `docs/reports/M2.8_business_knowledge_acquisition.md`

> **Nunca se actualiza un documento maestro directamente desde las notas sin pasar por revisión y aprobación.**

---

## 12. CJ Knowledge Engineering Framework

> **El verdadero producto no es solo CJ_OS. Es una metodología para capturar, validar y estructurar el conocimiento de cualquier empresa antes de automatizarla.**

Ese framework es reutilizable independientemente de la tecnología subyacente (n8n, IA, PostgreSQL o futuras herramientas).

---

## Historial de cambios

| Fecha | Versión | Cambio |
|-------|---------|--------|
| 2026-06-25 | 0.1.0 | Creación del Knowledge Acquisition Protocol (KAP): tipos de conocimiento, metadatos, protocolo paso a paso, criterios de cierre, niveles de confianza e identificadores. |
| 2026-06-25 | 0.2.0 | Agregado KES-0 de lenguaje empresarial, separación de etapas (notas temporales → revisión → aprobación → documentos oficiales), estados extendidos del conocimiento, criticalidad y capas de conocimiento. |
| 2026-06-25 | 0.3.0 | Agregado Knowledge Evidence Standard, tipos de sesión KES-D/I/O/V, metadatos de evidencia y concepto de activos de conocimiento. |
| 2026-06-25 | 0.4.0 | Agregadas métricas de éxito de KES, mantenimiento de Known Unknowns y Assumptions Register, y alineación con Architecture Freeze. |
| 2026-06-25 | 0.5.0 | Reemplazado Architecture Freeze por Controlled Evolution, agregada naturaleza del conocimiento (universal/específico/estratégico), estabilidad (estable/variable/temporal/experimental), KES-Pilot y enfoque de descubrimiento. |
| 2026-06-25 | 0.6.0 | KES-Pilot redefinida como prueba de un solo proceso (entrada de mercancía), agregadas métricas de densidad y reutilización, y cuatro preguntas post-KES. |
| 2026-06-25 | 0.7.0 | Agregado Knowledge Quality Score (KQS), ciclo de vida extendido del conocimiento, separación observación/patrón/buena práctica/regla, pregunta de sabiduría y criterio de comprensión externa en KES-Pilot. |
