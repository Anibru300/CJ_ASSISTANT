# Business Dictionary — CJ_OS

**Versión:** 0.3.0  
**Fecha:** 2026-06-26  
**Estado:** Enriquecido con términos validados en KES-Pilot de entrada de mercancía  
**Propósito:** Construir el **lenguaje corporativo estándar de 3P** para que personas, procesos, agentes de IA y documentos usen el mismo significado.

---

## 1. Principio fundamental

> **Antes de modelar procesos, hay que modelar palabras.**

Si cada persona usa términos distintos, la IA recibirá mensajes ambiguos y generará decisiones incorrectas. Este diccionario es la **fuente de verdad del lenguaje de la empresa**.

> **KES-0 no solo valida términos. Construye el lenguaje oficial de 3P** que usarán CJ_OS, el SGC, capacitaciones, reportes, dashboards, workflows de n8n, tablas de PostgreSQL y prompts de IA.

---

## 2. Estructura de cada término

Cada entrada del diccionario contiene:

| Campo | Descripción |
|-------|-------------|
| **Nombre oficial** | La palabra o frase aprobada. |
| **Definición** | Significado exacto dentro de 3P. |
| **Sinónimos aceptados** | Variantes que se pueden usar sin cambiar el sentido. |
| **Lo que NO significa** | Términos cercanos que deben evitarse en este contexto. |
| **Dominio** | Área(s) donde aplica principalmente. |
| **Objetos relacionados** | Entidades de la ontología vinculadas. |
| **Estado** | Descubierto / Documentado / Revisado / Validado / Implementado / Obsoleto. |
| **KES de origen** | Sesión donde se definió. |
| **Propietario** | Quién garantiza que la definición sigue vigente. |

---

## 3. Términos iniciales

### Vale

| Campo | Valor |
|-------|-------|
| **Nombre oficial** | Vale |
| **Definición** | Documento interno que registra la salida de material del almacén hacia otro departamento, proceso o cliente. |
| **Sinónimos aceptados** | Vale de almacén, ticket de salida. |
| **Lo que NO significa** | Orden de compra, factura, pedido de cliente, remisión. |
| **Dominio** | Almacén, Ventas, Logística, Contabilidad. |
| **Objetos relacionados** | Producto, Usuario, Movimiento, Rack, Existencia. |
| **Estado** | Documentado |
| **KES de origen** | KES-0 (pendiente) |
| **Propietario** | Salvador / Francisco |

---

### Solicitud

| Campo | Valor |
|-------|-------|
| **Nombre oficial** | Solicitud |
| **Definición** | Petición formal de material, servicio o acción que aún no se autoriza ni ejecuta. |
| **Sinónimos aceptados** | Requisición, petición. |
| **Lo que NO significa** | Orden de compra, vale, pedido confirmado. |
| **Dominio** | Todos. |
| **Objetos relacionados** | Usuario, Producto, Aprobación, Pedido. |
| **Estado** | Documentado |
| **KES de origen** | KES-0 (pendiente) |
| **Propietario** | Carlos |

---

### Pedido

| Campo | Valor |
|-------|-------|
| **Nombre oficial** | Pedido |
| **Definición** | Requerimiento de productos hecho por un cliente o área interna, que inicia un flujo de surtido o venta. |
| **Sinónimos aceptados** | Orden de cliente, orden de pedido. |
| **Lo que NO significa** | Orden de compra (es al proveedor), solicitud (no comprometida), vale (es salida de almacén). |
| **Dominio** | Ventas, Almacén, Logística. |
| **Objetos relacionados** | Cliente, Producto, Vale, Factura, Entrega. |
| **Estado** | Documentado |
| **KES de origen** | KES-0 (pendiente) |
| **Propietario** | Responsable de Ventas |

---

### Orden de compra

| Campo | Valor |
|-------|-------|
| **Nombre oficial** | Orden de compra |
| **Definición** | Documento dirigido a un proveedor para adquirir bienes o servicios, con cantidades, precios y condiciones acordadas. |
| **Sinónimos aceptados** | OC, orden de proveedor. |
| **Lo que NO significa** | Pedido de cliente, factura, recepción, vale. |
| **Dominio** | Compras, Almacén, Contabilidad. |
| **Objetos relacionados** | Proveedor, Producto, Entrada, Factura, Pago. |
| **Estado** | Documentado |
| **KES de origen** | KES-0 (pendiente) |
| **Propietario** | Responsable de Compras |

---

### Entrada

| Campo | Valor |
|-------|-------|
| **Nombre oficial** | Entrada |
| **Definición** | Registro del ingreso de mercancía al almacén, usualmente asociado a una recepción de compra. |
| **Sinónimos aceptados** | Entrada de almacén, entrada de mercancía. |
| **Lo que NO significa** | Salida, vale, pedido, embarque. |
| **Dominio** | Almacén, Compras, Logística. |
| **Objetos relacionados** | Producto, Rack, Existencia, Orden de compra, Recepción. |
| **Estado** | Documentado |
| **KES de origen** | KES-0 (pendiente) |
| **Propietario** | Salvador / Francisco |

---

### Recepción

| Campo | Valor |
|-------|-------|
| **Nombre oficial** | Recepción |
| **Definición** | Acción física de recibir mercancía, verificar cantidades, calidad y documentos, y decidir si se acepta. |
| **Sinónimos aceptados** | Recepción de mercancía. |
| **Lo que NO significa** | Entrada (la recepción puede resultar en rechazo; la entrada implica ingreso al almacén), embarque. |
| **Dominio** | Almacén, Calidad, Compras. |
| **Objetos relacionados** | Producto, Proveedor, Orden de compra, Entrada, Merma, Evidencia. |
| **Estado** | Documentado |
| **KES de origen** | KES-0 (pendiente) |
| **Propietario** | Salvador / Francisco |

---

### Surtido

| Campo | Valor |
|-------|-------|
| **Nombre oficial** | Surtido |
| **Definición** | Acción de preparar y entregar los productos solicitados por un pedido o vale. |
| **Sinónimos aceptados** | Preparación de pedido, picking. |
| **Lo que NO significa** | Embarque (el surtido es interno; el embarque es envío al cliente), compra, recepción. |
| **Dominio** | Almacén, Ventas, Logística. |
| **Objetos relacionados** | Pedido, Vale, Producto, Rack, Existencia, Entrega. |
| **Estado** | Documentado |
| **KES de origen** | KES-0 (pendiente) |
| **Propietario** | Salvador / Francisco |

---

### Embarque

| Campo | Valor |
|-------|-------|
| **Nombre oficial** | Embarque |
| **Definición** | Acción de enviar mercancía al cliente o destino final, después del surtido. |
| **Sinónimos aceptados** | Envío, salida de transporte. |
| **Lo que NO significa** | Surtido, recepción, vale. |
| **Dominio** | Logística, Ventas, Almacén. |
| **Objetos relacionados** | Pedido, Transporte, Cliente, Entrega, Guía. |
| **Estado** | Documentado |
| **KES de origen** | KES-0 (pendiente) |
| **Propietario** | Responsable de Logística |

---

### Existencia

| Campo | Valor |
|-------|-------|
| **Nombre oficial** | Existencia |
| **Definición** | Cantidad física de un producto disponible en el almacén en un momento determinado. |
| **Sinónimos aceptados** | Inventario físico, cantidad en stock. |
| **Lo que NO significa** | Stock comprometido, stock disponible para venta, demanda. |
| **Dominio** | Almacén, Compras, Ventas, Contabilidad. |
| **Objetos relacionados** | Producto, Rack, Lote, Movimiento, Inventario. |
| **Estado** | Documentado |
| **KES de origen** | KES-0 (pendiente) |
| **Propietario** | Salvador / Francisco |

---

### Stock

| Campo | Valor |
|-------|-------|
| **Nombre oficial** | Stock |
| **Definición** | Representación numérica de la cantidad de producto registrada en el sistema, que puede incluir disponible, comprometido, en tránsito o en merma. |
| **Sinónimos aceptados** | Saldo, inventario registrado. |
| **Lo que NO significa** | Existencia física (puede diferir por errores, mermas o tránsito). |
| **Dominio** | Almacén, Compras, Ventas, Contabilidad. |
| **Objetos relacionados** | Producto, Existencia, Lote, Movimiento, SAE. |
| **Estado** | Documentado |
| **KES de origen** | KES-0 (pendiente) |
| **Propietario** | Salvador / Francisco |

---

## 4. Plantilla para agregar nuevos términos

```markdown
### [Nombre oficial]

| Campo | Valor |
|-------|-------|
| **Nombre oficial** | |
| **Definición** | |
| **Sinónimos aceptados** | |
| **Lo que NO significa** | |
| **Dominio** | |
| **Objetos relacionados** | |
| **Estado** | Documentado |
| **KES de origen** | KES-0 |
| **Propietario** | |
```

---

## 5. Reglas de uso

1. **Este diccionario es maestro.** Los demás documentos deben usar los términos oficiales.
2. **Si un término no está aquí, no se usa en documentación oficial hasta ser definido.**
3. **Cada KES debe confirmar o descubrir nuevos términos.**
4. **Un término solo pasa a Validado tras acuerdo del propietario del dominio y Carlos.**

---

## Historial de cambios

| Fecha | Versión | Cambio |
|-------|---------|--------|
| 2026-06-25 | 0.1.0 | Creación del Business Dictionary con términos iniciales de Almacén, Compras, Ventas y Logística. |
| 2026-06-25 | 0.2.0 | Reforzado el objetivo de KES-0: construir lenguaje corporativo estándar, no solo validar términos. |

---

### Sub-almacén

| Campo | Valor |
|-------|-------|
| **Nombre oficial** | Sub-almacén |
| **Definición** | Ubicación lógica de inventario asociada a un proveedor específico, dentro del almacén general de 3P. Ejemplos: A-1 ROXELL, A-2 LUBING. |
| **Sinónimos aceptados** | Almacén de proveedor, ubicación de inventario. |
| **Lo que NO significa** | Rack físico, bodega de terceros, zona de cuarentena. |
| **Dominio** | Almacén, Compras, Logística. |
| **Objetos relacionados** | Producto, Ubicación, Proveedor, Existencia. |
| **Estado** | Validado |
| **KES de origen** | KES-Pilot entrada de mercancía (2026-06-26) |
| **Propietario** | Salvador / Francisco |

---

### Cantidad viva

| Campo | Valor |
|-------|-------|
| **Nombre oficial** | Cantidad viva |
| **Definición** | Cantidad de un vale de salida que aún no se ha facturado ni vendido, pero que sigue formando parte del inventario de 3P para fines de conteo. |
| **Sinónimos aceptados** | Cantidad pendiente de facturar. |
| **Lo que NO significa** | Cantidad disponible para venta, cantidad física en almacén, stock comprometido. |
| **Dominio** | Almacén, Ventas, Contabilidad. |
| **Objetos relacionados** | Vale, Vale línea, Producto, Existencia. |
| **Estado** | Validado |
| **KES de origen** | KES-Pilot entrada de mercancía (2026-06-26) |
| **Propietario** | Salvador / Francisco |

---

### Logística y Compras

| Campo | Valor |
|-------|-------|
| **Nombre oficial** | Logística y Compras |
| **Definición** | Puesto combinado en 3P responsable de compras nacionales e internacionales, coordinación de envíos, aviso de arribos a Almacén y registro de entradas en Aspel-SAE. |
| **Sinónimos aceptados** | Compras, Logística. |
| **Lo que NO significa** | Almacén, Contabilidad, Ventas. |
| **Dominio** | Compras, Logística, Almacén. |
| **Objetos relacionados** | Proveedor, Orden de compra, Entrada, SAE. |
| **Estado** | Validado |
| **KES de origen** | KES-Pilot entrada de mercancía (2026-06-26) |
| **Propietario** | Carlos |

---

### Recepción

| Campo | Valor |
|-------|-------|
| **Nombre oficial** | Recepción |
| **Definición** | Acción física de recibir mercancía del transportista, contarla, inspeccionarla, documentarla con fotografías y entregar reporte a Logística. |
| **Sinónimos aceptados** | Recepción de mercancía. |
| **Lo que NO significa** | Entrada en SAE (eso lo hace Logística), embarque, surtido. |
| **Dominio** | Almacén, Calidad, Compras. |
| **Objetos relacionados** | Producto, Proveedor, Orden de compra, Entrada, Merma, Evidencia. |
| **Estado** | Validado |
| **KES de origen** | KES-Pilot entrada de mercancía (2026-06-26) |
| **Propietario** | Salvador / Francisco |

---

### Cuarentena

| Campo | Valor |
|-------|-------|
| **Nombre oficial** | Cuarentena |
| **Definición** | Estado temporal en el que se coloca mercancía en espera de inspección, decisión de aceptación o resolución de discrepancia. Típicamente 1-2 días. |
| **Sinónimos aceptados** | Zona de cuarentena, material en revisión. |
| **Lo que NO significa** | Merma, rechazo definitivo, sub-almacén permanente. |
| **Dominio** | Almacén, Calidad. |
| **Objetos relacionados** | Producto, Ubicación, Inspección, No conformidad. |
| **Estado** | Validado |
| **KES de origen** | KES-Pilot entrada de mercancía (2026-06-26) |
| **Propietario** | Salvador / Francisco |

---

### Mini-SAE

| Campo | Valor |
|-------|-------|
| **Nombre oficial** | Mini-SAE |
| **Definición** | Hoja de Excel que concentra el inventario general de 3P, extraído de Aspel-SAE, y que debe reflejar la suma de las existencias de todos los sub-almacenes. |
| **Sinónimos aceptados** | Inventario general, concentrado de existencias. |
| **Lo que NO significa** | Sub-almacén, reporte de contabilidad, base de datos de SAE. |
| **Dominio** | Almacén, Contabilidad, Logística. |
| **Objetos relacionados** | Producto, Existencia, Sub-almacén, SAE. |
| **Estado** | Validado |
| **KES de origen** | KES-Pilot entrada de mercancía (2026-06-26) |
| **Propietario** | Salvador / Francisco |

---

*Diccionario actualizado tras KES-Pilot de entrada de mercancía.*
