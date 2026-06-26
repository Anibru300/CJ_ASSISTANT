# KES-Pilot — Entrada de mercancía de proveedor

**Fecha:** 2026-06-26  
**Sesión:** KES-Pilot (validación metodológica)  
**Proceso:** Entrada de mercancía de proveedor y asignación a sub-almacenes  
**Dominio:** Almacén / Compras / Calidad / Logística  
**Participantes sugeridos:** Carlos, Salvador (Jefe de Almacén), Francisco (Auxiliar de Almacén), Comprador, Logística.  
**Duración objetivo:** 30–45 minutos  
**Estado:** ✅ Completada — respuestas de Carlos registradas el 26/06/2026

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
| ¿Qué lo inicia? | Proveedor confirma envío. Logística y Compras (mismo puesto) avisa a Almacén. |
| ¿Qué lo termina? | Almacén sabe que llegará mercancía. |
| ¿Qué información consume? | OC, proveedor, cantidad estimada, fecha/hora. |
| ¿Qué información produce? | Notificación interna (correo/mensaje). |
| ¿Qué evento genera? | `llego_mercancia` |

### P2 — Recepción física y reporte a Logística

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Llegada del transporte al almacén. |
| ¿Qué lo termina? | Almacén entrega a Logística el reporte de recepción (conforme, faltante, sobrante o daño) y la factura firmada. |
| ¿Qué información consume? | Factura, nota de remisión/CP, OC. |
| ¿Qué información produce? | Reporte de recepción, factura firmada, evidencia fotográfica. |
| ¿Qué evento genera? | `se_inicio_recepcion` |

### P3 — Entrada en SAE

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Almacén termina de revisar el material y entrega reporte a Logística. |
| ¿Qué lo termina? | Logística registra la entrada en Aspel-SAE. |
| ¿Qué información consume? | Factura firmada, reporte de recepción de Almacén, OC. |
| ¿Qué información produce? | Entrada registrada en SAE; existencias en SAE se actualizan automáticamente. |
| ¿Qué evento genera? | `se_registro_entrada_en_sae` |

### P4 — Decisión de aceptación y asignación a sub-almacén

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Resultado de recepción física y discrepancias detectadas. |
| ¿Qué lo termina? | Decisión: aceptar, aceptar con nota, rechazar; y asignación de sub-almacén por proveedor. |
| ¿Qué información consume? | Discrepancias (faltante/sobrante), daños, evidencia fotográfica, proveedor del producto. |
| ¿Qué información produce? | Decisión documentada, sub-almacén destino, notificación a Logística/Compras. |
| ¿Qué evento genera? | `mercancia_aprobada` / `mercancia_rechazada`, `se_asigno_subalmacen` |

### P5 — Entrada al sub-almacén y actualización del Excel

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué lo inicia? | Aprobación de recepción y asignación de sub-almacén. |
| ¿Qué lo termina? | Mercancía en ubicación del sub-almacén y Excel actualizado (hoja del sub-almacén + Mini-SAE). |
| ¿Qué información consume? | Productos, cantidades, sub-almacén destino. |
| ¿Qué información produce? | Vale de entrada, actualización de existencias en sub-almacén y Mini-SAE (mediante macro). |
| ¿Qué evento genera? | `se_genero_vale_entrada`, `se_actualizo_existencia` |

---

## 7. Reglas del proceso

| # | Regla | Tipo | ¿Se puede romper? | Quién autoriza excepción |
|---|-------|------|-------------------|--------------------------|
| R1 | Toda entrada requiere OC o autorización previa. | Integridad | No | — |
| R2 | La cantidad recibida debe coincidir con factura/remisión. | Integridad | Con nota | Jefe de Almacén + Compras |
| R3 | Producto dañado se reporta a Logística; la aceptación parcial es posible. | Calidad | Solo con excepción documentada | Logística / Gerencia |
| R4 | Toda recepción debe generar evidencia fotográfica. | Flujo | No | — |
| R5 | Vale de entrada se genera solo después de aprobación. | Flujo | No | — |
| R6 | Cada producto se asigna a un sub-almacén según proveedor. | Flujo | Solo con autorización | Jefe de Almacén |
| R7 | Mini-SAE debe reflejar la suma de existencias de todos los sub-almacenes. | Integridad | No | — |
| R8 | El Excel de almacén se actualiza diariamente por el Jefe de Almacén. | Flujo | No | — |

---

## 8. Excepciones frecuentes

| Excepción | Causa | Acción |
|-----------|-------|--------|
| Material faltante o sobrante | Error de surtido del proveedor | Reportar a Logística; ella lo arregla con el proveedor. |
| Cantidad mayor a lo pedido | Error de surtido del proveedor | Se queda el excedente y Logística solicita factura del sobrante. |
| Producto dañado en tránsito | Transporte deficiente | Tomar evidencia, separar, gestionar con proveedor/seguro. |
| Producto no coincide con OC | Error de proveedor | Reportar a Logística; ella lo arregla con el proveedor. |
| Producto nuevo sin sub-almacén asignado | Nuevo código o proveedor | Jefe de Almacén decide asignación según proveedor. |
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

## 13. Respuestas completas de Carlos (26/06/2026)

### Sobre el arribo
1. **¿Cómo se entera el almacén de que va a llegar mercancía?**  
   Logística avisa a Almacén. El puesto de Logística también hace Compras (nacional e internacional).
2. **¿La mercancía llega siempre con OC?**  
   Sí, Almacén siempre tiene la OC o la factura de lo que va a llegar porque Logística se la proporciona.
3. **¿Quién recibe físicamente al transportista?**  
   Almacén. Le pide la documentación y después pasa a Logística el reporte de recepción (conforme, faltante, sobrante o daño) y la factura firmada.

### Sobre SAE
4. **¿Quién registra la entrada en SAE y cuándo?**  
   Logística. Lo hace cuando Almacén termina de revisar el material que llegó.
5. **¿SAE actualiza automáticamente las existencias?**  
   Sí.
6. **¿El almacén consulta SAE?**  
   Principalmente lo usan Ventas, Facturación, Logística y Contabilidad. Almacén solo hace consultas o ve movimientos.

### Sobre el conteo e inspección
7. **¿Quién cuenta la mercancía y cómo?**  
   Almacén (Jefe y Auxiliar). Varía según cómo llegue: emplaye, caja, tarima o contenedor.
8. **¿Se toman fotos?**  
   Se toman fotos en cada recepción. (O debería hacerse.)
9. **¿Qué pasa si llega dañada una parte y el resto bien?**  
   Se acepta, pero se reporta a Logística y ella lo arregla con el proveedor.

### Sobre sub-almacenes
10. **¿Cómo se decide a qué sub-almacén va cada producto?**  
    Por proveedor. Si el proveedor es LUBING, va al sub-almacén de LUBING.
11. **¿Un mismo producto puede estar en varios sub-almacenes?**  
    Sí, cuando un producto puede ser surtido por varios proveedores diferentes.
12. **¿Qué pasa si llega un producto nuevo sin sub-almacén?**  
    Se ve de qué proveedor es y se asigna al almacén de ese proveedor.

### Sobre el Excel
13. **¿Quién y cuándo actualiza el Excel?**  
    El Jefe de Almacén lo actualiza diariamente.
14. **¿Se actualiza primero el sub-almacén o Mini-SAE?**  
    Al mismo tiempo. Hay una macro que actualiza ambos porque es la misma información.
15. **¿El Excel y SAE no coinciden?**  
    Sí pasa seguido. Se identifica por qué y se hacen ajustes.

### Sobre excepciones
16. **¿Excepción más frecuente?**  
    Material faltante o sobrante.
17. **¿Cuánto tiempo en cuarentena?**  
    1 o 2 días en lo que se revisa.
18. **¿Qué pasa si mandan más de lo pedido?**  
    Se queda el excedente y Logística reporta al proveedor para que facture el sobrante.

### Sobre decisiones
19. **¿Quién decide aceptar mercancía con discrepancia?**  
    Logística o Gerencia.
20. **¿Productos con inspección especial?**  
    Sí, detergentes (líquidos) y productos frágiles.

---

## 14. Resultados esperados de la KES-Pilot

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
