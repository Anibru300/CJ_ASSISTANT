# KES-Pilot — Entrada de mercancía de proveedor

**Fecha:** 2026-06-26  
**Sesión:** KES-Pilot (validación metodológica)  
**Proceso:** Entrada de mercancía de proveedor y asignación a sub-almacenes  
**Dominio:** Almacén / Compras / Calidad / Logística  
**Participantes sugeridos:** Carlos, Salvador (Jefe de Almacén), Francisco (Auxiliar de Almacén), Comprador, Logística.  
**Duración objetivo:** 30–45 minutos  
**Estado:** 🔄 En ejecución — cuestionario preparado para Carlos/Salvador/Francisco

---

## 1. Objetivo de la KES-Pilot

Validar que la metodología CJ_OS de extracción de conocimiento puede modelar un proceso real de 3P en 30–45 minutos, llenando todos los artefactos requeridos:

- Objetos (entidades)
- Eventos
- Proceso con 5 preguntas
- Reglas
- Decisiones
- Excepciones
- KPIs
- Pregunta de sabiduría

Si algo no tiene lugar, se ajusta la metodología antes de KES-0.

---

## 2. Proceso seleccionado

**Entrada de mercancía de proveedor y asignación a sub-almacenes** — desde que Logística registra la entrada en SAE hasta que la mercancía queda disponible en el sub-almacén correspondiente (A-1 ROXELL, A-2 LUBING, etc.) y reflejada en el inventario general (Mini-SAE).

Se eligió porque:
- Es un proceso diario en 3P.
- Actualmente se captura en SAE, pero el control de sub-almacenes se hace en Excel.
- Es el primer puente natural entre CJ_OS y los sistemas existentes.
- Tiene reglas claras y excepciones frecuentes.
- Ya existe documentación previa: `workspace/shared/kes_notes/PR-ALM-001-V3_Recepcion_Mercancia.txt` y `docs/reports/BD_ALMACEN_3P_analysis.md`.

---

## 3. Actores

| Rol | Responsabilidad en este proceso |
|-----|----------------------------------|
| **Proveedor** | Entrega mercancía con documentación. |
| **Transportista** | Lleva la mercancía física. |
| **Logística** | Registra la entrada en SAE; coordina arribo. |
| **Jefe de Almacén** | Supervisa recepción, autoriza desviaciones, decide sub-almacén. |
| **Auxiliar de Almacén** | Recibe, cuenta, inspecciona, traslada a sub-almacén, actualiza Excel. |
| **Comprador** | Resuelve discrepancias con proveedor. |
| **Inspector de Calidad** | Verifica conformidad si aplica. |

---

## 4. Objetos / entidades involucradas

| Entidad | Uso en este proceso |
|---------|---------------------|
| `Orden de compra (OC)` | Documento base contra el que se recibe. |
| `Factura del proveedor` | Evidencia fiscal y de contenido. |
| `Nota de remisión / carta porte` | Documento de transporte. |
| `Producto` | Lo que se recibe. |
| `Sub-almacén / Ubicación` | Donde se coloca (A-1 ROXELL, A-2 LUBING, etc.). |
| `Existencia` | Stock que se actualizará. |
| `Vale de entrada` | Movimiento de entrada formal. |
| `Evidencia fotográfica` | Fotos de empaque, daños, discrepancias. |
| `No conformidad` | Si la mercancía no cumple estándar. |
| `Merma` | Si se rechaza o daña material. |

---

## 5. Eventos identificados

| Evento | Significado |
|--------|-------------|
| `llego_mercancia` | El transporte está en almacén. |
| `se_registro_entrada_en_sae` | Logística capturó la entrada en Aspel-SAE. |
| `se_inicio_recepcion` | Auxiliar comienza revisión documental y física. |
| `se_detecto_desfase` | Cantidad o producto no coincide con OC/factura. |
| `se_detecto_dano` | Empaque o contenido dañado. |
| `mercancia_aprobada` | Pasa inspección y se autoriza entrada. |
| `mercancia_rechazada` | No se acepta; genera merma o devolución. |
| `se_asigno_subalmacen` | Se decide a qué sub-almacén va cada producto. |
| `se_genero_vale_entrada` | Entrada formal al sub-almacén. |
| `se_actualizo_existencia` | Stock del sub-almacén y Mini-SAE actualizado. |

---

## 6. Proceso detallado (AS-IS)

### P1 — Notificación de arribo

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Proveedor confirma envío → Logística notifica. |
| ¿Qué lo termina? | Jefe de Almacén sabe que llegará mercancía. |
| ¿Qué información consume? | OC, proveedor, cantidad estimada, fecha/hora. |
| ¿Qué información produce? | Notificación interna (correo/mensaje). |
| ¿Qué evento genera? | `llego_mercancia` |

### P2 — Entrada en SAE

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Llegada del transporte y documentos completos. |
| ¿Qué lo termina? | Logística registra la entrada en Aspel-SAE. |
| ¿Qué información consume? | Factura, nota de remisión, OC. |
| ¿Qué información produce? | Entrada registrada en SAE, existencia actualizada en SAE. |
| ¿Qué evento genera? | `se_registro_entrada_en_sae` |

### P3 — Recepción física en almacén

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Entrada registrada en SAE. |
| ¿Qué lo termina? | Conteo físico e inspección de empaque realizados. |
| ¿Qué información consume? | OC, factura, producto físico. |
| ¿Qué información produce? | Conteo real, evidencia fotográfica, checklist. |
| ¿Qué evento genera? | `se_inicio_recepcion` |

### P4 — Decisión de aceptación y asignación a sub-almacén

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Resultado de inspección física. |
| ¿Qué lo termina? | Decisión: aceptar, aceptar con nota, rechazar; y asignación de sub-almacén. |
| ¿Qué información consume? | Discrepancias, daños, evidencia, proveedor asociado al producto. |
| ¿Qué información produce? | Decisión documentada, sub-almacén destino, correo a compras/logística. |
| ¿Qué evento genera? | `mercancia_aprobada` / `mercancia_rechazada`, `se_asigno_subalmacen` |

### P5 — Entrada al sub-almacén

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Aprobación de recepción y asignación de sub-almacén. |
| ¿Qué lo termina? | Mercancía en ubicación del sub-almacén y Excel actualizado. |
| ¿Qué información consume? | Productos, cantidades, sub-almacén destino. |
| ¿Qué información produce? | Vale de entrada, actualización de existencias en sub-almacén y Mini-SAE. |
| ¿Qué evento genera? | `se_genero_vale_entrada`, `se_actualizo_existencia` |

---

## 7. Reglas del proceso

| # | Regla | Tipo | ¿Se puede romper? | Quién autoriza excepción |
|---|-------|------|-------------------|--------------------------|
| R1 | Toda entrada requiere OC o autorización previa. | Integridad | No | — |
| R2 | La cantidad recibida debe coincidir con factura/remisión. | Integridad | Con nota | Jefe de Almacén + Compras |
| R3 | Producto dañado no entra a inventario. | Calidad | Solo con excepción documentada | Jefe de Almacén + Calidad |
| R4 | Toda discrepancia requiere evidencia fotográfica. | Flujo | No | — |
| R5 | Vale de entrada se genera solo después de aprobación. | Flujo | No | — |
| R6 | Cada producto se asigna a un sub-almacén según proveedor/clasificación. | Flujo | Solo con autorización | Jefe de Almacén |
| R7 | Mini-SAE debe reflejar la suma de existencias de todos los sub-almacenes. | Integridad | No | — |

---

## 8. Excepciones frecuentes

| Excepción | Causa | Acción |
|-----------|-------|--------|
| Mercancía sin OC | Error de proveedor o compras urgentes | Detener, notificar a Compras, esperar autorización. |
| Cantidad mayor a lo pedido | Error de surtido del proveedor | Aceptar solo con nota y autorización; rechazar excedente. |
| Producto dañado en tránsito | Transporte deficiente | Tomar evidencia, separar, gestionar con proveedor/seguro. |
| Producto no coincide con OC | Error de proveedor | Detener, documentar, esperar instrucciones de Compras. |
| Falta certificado de calidad | Documentación incompleta | Registrar observación, notificar, condicionar entrada. |
| Producto sin sub-almacén definido | Nuevo código o proveedor | Jefe de Almacén decide asignación; registrar en catálogo. |

---

## 9. Decisiones clave

| Decisión | Información necesaria | Opciones | Responsable |
|----------|----------------------|----------|-------------|
| ¿Aceptar mercancía con discrepancy? | Evidencia, monto, impacto | Aceptar con nota / Rechazar / Aceptar condicional | Jefe de Almacén + Compras |
| ¿Ingresar material sin OC? | Urgencia, autorización por escrito | Sí, con autorización / No | Director / Compras |
| ¿Aplicar merma? | Cantidad dañada, causa, evidencia | Sí / No | Jefe de Almacén + Calidad |
| ¿A qué sub-almacén se asigna? | Proveedor, tipo de producto, existencias actuales | Sub-almacén específico / Cuarentena | Jefe de Almacén |
| ¿Ubicar en zona de cuarentena? | Estado de inspección | Sí / No | Inspector de Calidad |

---

## 10. KPIs propuestos

| KPI | Meta | Fuente |
|-----|------|--------|
| Recepciones conformes | ≥ 98% | Reportes de recepción |
| Tiempo promedio de recepción | ≤ 2 horas | Timestamp de eventos |
| Precisión documental | 100% | Checklist de documentos |
| Mermas por recepción | < 1% | Registros de merma |
| Sub-almacenes actualizados al día | 100% | Comparación Mini-SAE vs. sub-almacenes |

---

## 11. Pregunta de sabiduría

> **Si mañana contrataras a un nuevo gerente de almacén, ¿qué le explicarías sobre la recepción de mercancía que no aparece en ningún procedimiento escrito?**

Ejemplos de respuestas esperadas:
- Cómo identificar un proveedor problemático antes de que llegue la mercancía.
- Cuándo es mejor aceptar con nota y cuándo es mejor rechazar.
- Cómo negociar con transportistas para minimizar daños.
- Cómo decidir a qué sub-almacén va un producto nuevo.

---

## 12. Cuestionario práctico para la sesión

Responder con la operación real de 3P, no con el procedimiento ideal.

### Sobre el arribo
1. ¿Cómo se entera el almacén de que va a llegar mercancía? ¿Quién avisa y por qué medio?
2. ¿La mercancía llega siempre con OC, o a veces llega sin ella? ¿Qué pasa en ese caso?
3. ¿Quién recibe físicamente al transportista? ¿Qué documentos le pide?

### Sobre SAE
4. ¿Quién registra la entrada en SAE? ¿En qué momento lo hace: al llegar, al terminar de contar, o al día siguiente?
5. ¿SAE ya actualiza automáticamente las existencias, o hay que hacer otro paso?
6. ¿El almacén consulta SAE para saber qué entró, o SAE solo lo usa contabilidad/logística?

### Sobre el conteo e inspección
7. ¿Quién cuenta la mercancía? ¿Se cuenta pieza por pieza o por caja/pallet?
8. ¿Se toman fotos siempre, solo cuando hay daño, o solo cuando hay discrepancia?
9. ¿Qué pasa si llega dañada una parte y el resto bien? ¿Se acepta parcialmente?

### Sobre sub-almacenes
10. ¿Cómo decide el almacén a qué sub-almacén (A-1, A-2, etc.) va cada producto?
11. ¿Un mismo producto puede estar en varios sub-almacenes? ¿Cómo se decide cuánto va a cada uno?
12. ¿Qué pasa si llega un producto nuevo que no tiene sub-almacén asignado?

### Sobre el Excel
13. ¿Quién y cuándo actualiza el Excel de almacén después de una entrada?
14. ¿Se actualiza primero la hoja del sub-almacén y después el Mini-SAE, o al revés?
15. ¿Alguna vez el Excel y SAE no coinciden? ¿Cómo se detecta y corrige?

### Sobre excepciones
16. ¿Cuál es la excepción más frecuente en recepción?
17. ¿Cuánto tiempo puede quedar mercancía en cuarentena?
18. ¿Qué pasa si un proveedor manda más de lo que se pidió? ¿Se regresa o se queda?

### Sobre decisiones
19. ¿Quién tiene la última palabra para aceptar mercancía con discrepancia?
20. ¿Hay productos que requieren inspección especial de calidad? ¿Cuáles y quién los revisa?

---

## 13. Resultados esperados de la KES-Pilot

Al finalizar la sesión se debe tener:

1. Confirmación de que la estructura de ficha maestra funciona.
2. Lista de términos que deben ir al Business Dictionary.
3. Identificación de reglas faltantes o contradictorias.
4. Confirmación de que el proceso genera eventos claros.
5. Decisión: ¿la metodología está lista para KES-0 o necesita ajustes?

---

## 14. Ajustes metodológicos pendientes

Después de la KES-Pilot, registrar aquí cualquier cambio necesario en:

- Estructura de la ficha maestra.
- Business Dictionary.
- Ontología.
- Knowledge Coverage Matrix.
- Protocolo KES.

________________________________________________________________________

________________________________________________________________________

---

*Documento generado por Kimi el 2026-06-26 como propuesta de KES-Pilot. Actualizado con enfoque real de entrada en SAE + asignación a sub-almacenes.*
