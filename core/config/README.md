# Core / Config

## Propósito

Gestión centralizada de la configuración de CJ_OS en runtime.

## Responsabilidades

- Cargar configuración desde `.env` y archivos en `config/`.
- Proveer configuración por ambiente: development, production, testing.
- Validar que las variables críticas estén presentes antes de iniciar servicios.
- Permitir recargar configuración sin reiniciar todo el sistema cuando sea posible.

## Fuentes de configuración

- `.env` — variables de entorno globales.
- `config/development/` — configuración de desarrollo.
- `config/production/` — configuración de producción.
- `config/testing/` — configuración de pruebas.

## Estado

- Fase M1.2.5: estructura y documentación listas.
