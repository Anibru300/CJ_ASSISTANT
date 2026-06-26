# Core / Memory

## Propósito

Gestión de la memoria operativa de CJ_OS.

## Responsabilidades

- Almacenar conversaciones activas y eventos recientes.
- Gestionar contexto de interacciones con usuarios.
- Recordar decisiones previas y sus resultados.
- Proveer acceso rápido al historial para el Motor de IA.
- Limpiar estados obsoletos según políticas de retención.

## Pregunta que responde

> **¿Qué pasó?**

## Ejemplo

- "Francisco pidió 50 tornillos ayer."
- "El cliente X rechazó la cotización del 15 de junio."

## Fuentes esperadas

- Redis para estados temporales y caché.
- PostgreSQL para contexto persistente.

## Estado

- Fase M2.1: estructura y documentación listas.
