# Core / Security

## Propósito

Seguridad transversal de CJ_OS.

## Responsabilidades

- Autenticación de usuarios, sistemas y servicios.
- Autorización y control de acceso.
- Cifrado de datos sensibles en reposo y en tránsito.
- Gestión de secretos y credenciales.
- Validación de entradas y prevención de ataques comunes.

## Reglas

- Las credenciales viven únicamente en `.env` y gestores de secretos.
- Nunca se escriben contraseñas, tokens ni claves en el código.
- Todo acceso al Core debe poder ser auditado.

## Estado

- Fase M1.2.5: estructura y documentación listas.
