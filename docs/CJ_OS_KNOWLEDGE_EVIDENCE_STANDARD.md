# Knowledge Evidence Standard — CJ_OS

**Versión:** 0.1.0  
**Abreviatura:** KES-EV o Evidence Standard  
**Fecha:** 2026-06-25  
**Estado:** Borrador inicial — pendiente de validación  
**Propósito:** Garantizar que ningún conocimiento entre a CJ_OS sin evidencia objetiva que lo respalde.

---

## 1. Principio fundamental

> **Sin evidencia no hay conocimiento. Solo hay opinión.**

CJ_OS no ejecutará, propondrá ni validará reglas, decisiones o automatizaciones basadas únicamente en recuerdos o suposiciones. Cada ítem de conocimiento debe tener una fuente de evidencia clasificada y un nivel de confianza asociado.

> **Nota sobre la abreviatura:** Para evitar confusión con *Knowledge Engineering Session (KES)*, este estándar se abrevia **KES-EV** o simplemente **Evidence Standard**.

---

## 2. Tipos de evidencia y nivel de confianza

| Tipo de evidencia | Descripción | Confianza base | Ejemplo |
|-------------------|-------------|----------------|---------|
| **Procedimiento oficial** | Documento aprobado por la empresa. | 100% | Manual de recepción de almacén firmado por Carlos. |
| **Política aprobada** | Regla de gobierno o política formal. | 100% | Política de no modificar vales cerrados. |
| **Manual** | Guía formal de operación. | 95% | Manual de usuario de SAE. |
| **Registro del ERP** | Dato extraído de SAE u otro ERP. | 95% | Reporte de existencias de SAE. |
| **Archivo Excel operativo** | Hoja de cálculo usada diariamente. | 90% | Excel de control de inventario. |
| **Observación directa** | El Knowledge Engineer vio el proceso. | 85% | Ver cómo Francisco recibe mercancía. |
| **Entrevista con responsable** | Declaración del líder del área. | 80% | Entrevista con Salvador. |
| **Entrevista con operador** | Declaración de quien ejecuta el proceso. | 70% | Entrevista con auxiliar de almacén. |
| **Suposición** | Inferencia sin respaldo documental ni testigo. | 20% | "Supongo que siempre se hace así." |

> **La confianza final puede ajustarse** según antigüedad, consistencia con otras fuentes o contexto.

---

## 3. Campo de evidencia en cada ítem de conocimiento

Cada pieza de conocimiento debe registrar:

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| **Evidencia** | Tipo de evidencia que respalda el conocimiento. | Procedimiento oficial |
| **Referencia** | Dónde encontrar la evidencia. | `procedimientos/almacen/recepcion_v1.2.pdf` |
| **Confianza base** | Confianza asociada al tipo de evidencia. | 100% |
| **Confianza ajustada** | Confianza final tras revisión. | 100% |
| **Recolectada en** | Sesión o actividad donde se obtuvo. | KES-D-01-ALM |
| **Responsable de evidencia** | Quién puede entregar o confirmar la evidencia. | Salvador |

---

## 4. Tipos de sesiones de recolección de evidencia

Cada sesión de adquisición de conocimiento puede tener uno o más tipos:

| Tipo | Nombre | Objetivo | Producto |
|------|--------|----------|----------|
| **KES-D** | Documental | Revisar procedimientos, formatos, políticas, SAE, Excel, correos. | Lista de evidencias documentales. |
| **KES-I** | Entrevista | Entrevistar a responsables y operadores. | Notas de entrevista con citas. |
| **KES-O** | Observación | Ver trabajar al área en condiciones reales. | Registro de observación directa. |
| **KES-V** | Validación | Presentar el conocimiento capturado al experto para confirmar o corregir. | Ítems validados o rechazados. |

> Una KES de dominio puede contener KES-D, KES-I, KES-O y KES-V en secuencia.

### Ejemplo de secuencia para Almacén

1. **KES-D-01-ALM:** revisar procedimientos, formatos, SAE, Excel de inventario.
2. **KES-I-01-ALM:** entrevistar a Francisco y Salvador.
3. **KES-O-01-ALM:** observar una recepción y un surtido reales.
4. **KES-V-01-ALM:** presentar el conocimiento capturado y pedir confirmación.

---

## 5. Reglas del Evidence Standard

1. **Ningún conocimiento pasa a estado `Validado` sin evidencia.**
2. **La evidencia debe ser referenciable.** Archivo, minuta, captura, registro, etc.
3. **Si hay evidencia contradictoria, se escala al propietario del dominio.**
4. **Las suposiciones (<50% confianza) no alimentan documentos maestros.**
5. **Cada KES debe indicar qué tipos de evidencia se recolectaron.**

---

## 6. Relación con el Cognitive Model

El Evidence Standard alimenta el modelo de incertidumbre:

| Confianza ajustada | Comportamiento de CJ_OS |
|--------------------|-------------------------|
| ≥ 95% | Ejecuta si la autonomía lo permite. |
| 80-94% | Propone con recomendación. |
| 50-79% | Pregunta o pide más evidencia. |
| < 50% | No decide. Marca como hipótesis. |

---

## 7. Plantilla de registro de evidencia

```markdown
### ID de conocimiento

| Campo | Valor |
|-------|-------|
| **Conocimiento** | |
| **Tipo** | Hecho / Regla / Heurística / Excepción |
| **Evidencia** | Procedimiento oficial / Política / Manual / ERP / Excel / Observación / Entrevista / Suposición |
| **Referencia** | |
| **Confianza base** | |
| **Confianza ajustada** | |
| **Recolectada en** | KES-D/I/O/V-<sesion> |
| **Responsable de evidencia** | |
```

---

## Historial de cambios

| Fecha | Versión | Cambio |
|-------|---------|--------|
| 2026-06-25 | 0.1.0 | Creación del Knowledge Evidence Standard: tipos de evidencia, niveles de confianza, tipos de sesión D/I/O/V y reglas de uso. |
