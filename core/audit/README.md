# Core / Audit

## Propósito

Auditoría completa de todo lo que ocurre en CJ_OS.

## Responsabilidades

- Registrar eventos relevantes del sistema.
- Registrar errores y excepciones.
- Registrar métricas de uso y rendimiento.
- Guardar snapshots de estados importantes.
- Permitir reconstruir cualquier decisión o acción tomada por el sistema.

## Estructura sugerida

```text
core/audit/
├── events/      # Registro de eventos procesados
├── errors/      # Errores y excepciones
├── metrics/     # Métricas de uso y rendimiento
└── snapshots/   # Snapshots de estado
```

## Principio

> Toda decisión debe poder reconstruirse.

## Estado

- Fase M1.2.5: estructura y documentación listas.
