# Assumptions Register — CJ_OS

**Versión:** 0.1.0  
**Fecha:** 2026-06-25  
**Estado:** Registro vivo — se actualiza durante cada KES  
**Propósito:** Registrar suposiciones que aún no han sido validadas, para evitar construir CJ_OS sobre premisas incorrectas.

---

## 1. Principio

> **Construir sobre suposiciones no validadas es construir sobre hielo.**

Toda suposición debe quedar explícita, ser validada o eliminada antes de que el conocimiento pase a estado `Validado`.

---

## 2. Plantilla

| ID | Suposición | Dominio | Impacto si es falsa | Responsable | Vía de validación | Estado |
|----|------------|---------|---------------------|-------------|-------------------|--------|
| AS-001 | Todo producto tiene un SKU. | Almacén | Alta | KES-D-01-ALM | Revisar catálogo de productos en SAE | Sin validar |

---

## 3. Registro inicial

| ID | Suposición | Dominio | Impacto si es falsa | Responsable | Vía de validación | Estado |
|----|------------|---------|---------------------|-------------|-------------------|--------|
| AS-001 | Todo producto tiene un SKU. | Almacén | Alta | KES-D-01-ALM | Revisar catálogo de productos en SAE | Sin validar |
| AS-002 | Toda entrada de mercancía tiene orden de compra asociada. | Almacén | Alta | KES-I-01-ALM | Entrevista con compras y almacén | Sin validar |
| AS-003 | Los vales cerrados nunca se modifican. | Almacén | Media | KES-D-01-ALM | Revisar procedimientos y políticas | Sin validar |
| AS-004 | Toda merma se registra el mismo día del evento. | Almacén | Media | KES-O-01-ALM | Observar proceso de merma | Sin validar |
| AS-005 | El inventario físico coincide con SAE al menos semanalmente. | Almacén | Alta | KES-D-01-ALM + KES-O-01-ALM | Revisar registros de inventario cíclico | Sin validar |

---

## 4. Estados

| Estado | Significado |
|--------|-------------|
| **Sin validar** | Aún no se ha comprobado. |
| **En validación** | Se está recolectando evidencia. |
| **Validada** | Se confirmó que es cierta. |
| **Eliminada** | Se comprobó que es falsa; se descarta o se transforma en regla/excepción. |

---

## 5. Reglas de uso

1. Toda suposición que aparezca durante el diseño se registra aquí.
2. Ningún conocimiento pasa a `Validado` si depende de una suposición `Sin validar`.
3. Una suposición falsa se convierte en excepción o regla validada.
4. Este registro se revisa antes de cerrar cada KES.

---

## Historial de cambios

| Fecha | Versión | Cambio |
|-------|---------|--------|
| 2026-06-25 | 0.1.0 | Creación del Assumptions Register con plantilla y suposiciones iniciales. |
