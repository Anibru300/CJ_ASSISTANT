# Arquitectura de n8n en CJ_OS

**Fecha:** 2026-06-25  
**Versión:** 0.0.9  
**Estado:** Desplegado y operativo

---

## 1. Principio arquitectónico

> **n8n = Orquestador**  
> **CJ_OS = Cerebro**

n8n no es el cerebro del sistema. Es el **orquestador visual y técnico** que mueve datos, dispara acciones y conecta canales con el Core de CJ_OS.

---

## 2. Función de n8n

n8n cumple las siguientes funciones dentro de CJ_OS:

| Función | Descripción |
|---------|-------------|
| Recepción de eventos externos | Escuchar webhooks desde WhatsApp, Outlook y otros conectores. |
| Enrutamiento inicial | Enviar el evento recibido al Core de CJ_OS para su clasificación. |
| Invocación del Core | Llamar a funciones del Core cuando se requiere procesamiento inteligente. |
| Invocación de conectores | Disparar acciones en sistemas externos: enviar mensaje, crear tarea, sincronizar archivo. |
| Ejecución de workflows transversales | Ejecutar workflows base definidos en `core/orchestrator/`. |
| Distribución de respuestas | Enviar respuestas generadas por el Core al canal correspondiente. |
| Tareas programadas simples | Recibir triggers del scheduler para ejecutar flujos puntuales. |

---

## 3. Responsabilidades de n8n

- Recibir mensajes, correos, archivos y eventos desde conectores externos.
- Publicar esos eventos en el Core de CJ_OS.
- Invocar endpoints internos del Core de forma controlada.
- Ejecutar flujos de integración aprobados (workflows).
- Enviar respuestas y notificaciones a los canales configurados.
- Registrar en el Core los resultados de sus ejecuciones para auditoría.

---

## 4. Responsabilidades que n8n NO tiene

n8n **no** es responsable de:

- Tomar decisiones de negocio complejas.
- Contener lógica de negocio específica de módulos (almacén, ventas, calidad, etc.).
- Gestionar memoria conversacional.
- Almacenar datos estructurados de forma permanente (eso es PostgreSQL).
- Definir seguridad, autenticación ni autorización del sistema.
- Auditar eventos (eso lo hace `core/audit/`).
- Gestionar configuración del sistema.
- Seleccionar qué agente de IA debe responder.

> n8n es el conductor de la orquesta. El Core es el director.

---

## 5. Interacción con CJ_OS

### Flujo principal

```text
WhatsApp
    │
    ▼
n8n (Orquestador)
    │
    ▼
CJ_OS Core
    │
    ├─ events/    ← encola y enruta el evento
    ├─ memory/    ← recupera contexto conversacional
    ├─ security/  ← valida permisos y autenticación
    └─ config/    ← carga configuración relevante
    │
    ▼
AI Layer (ai/agents/)
    │
    ▼
Módulo de negocio (modules/<area>/)
    │
    ▼
PostgreSQL
    │
    ▼
Respuesta
    │
    ▼
n8n (Orquestador)
    │
    ▼
WhatsApp / Outlook / Dashboard
```

### Cómo n8n se comunica con el Core

1. n8n recibe un evento externo (ej. mensaje de WhatsApp).
2. n8n publica el evento en el Core mediante una llamada al componente `core/events/`.
3. El Core clasifica el evento, recupera contexto y decide qué agente invocar.
4. El agente consulta el módulo de negocio correspondiente.
5. El módulo lee o escribe en PostgreSQL.
6. El Core genera una respuesta.
7. n8n recibe la respuesta del Core y la envía al canal de salida.
8. `core/audit/` registra toda la interacción.

---

## 6. Configuración de despliegue

### Base de datos

- n8n está configurado para usar **PostgreSQL**, no SQLite.
- Variables de entorno relevantes:
  - `DB_TYPE=postgresdb`
  - `DB_POSTGRESDB_HOST=postgres`
  - `DB_POSTGRESDB_PORT=5432`
  - `DB_POSTGRESDB_DATABASE=${POSTGRES_DB}`
  - `DB_POSTGRESDB_USER=${POSTGRES_USER}`
  - `DB_POSTGRESDB_PASSWORD=${POSTGRES_PASSWORD}`

### Autenticación

- n8n tiene activada la autenticación básica mediante `N8N_BASIC_AUTH_ACTIVE=true`.
- Credenciales gestionadas en `.env`.

### Encriptación

- `N8N_ENCRYPTION_KEY` se utiliza para proteger credenciales almacenadas en n8n.
- La clave debe ser segura y de al menos 32 caracteres en producción.

### Persistencia

- Volumen montado: `runtime/n8n:/home/node/.n8n`
- Los workflows, credenciales y configuraciones de n8n persisten fuera del contenedor.

### Red

- n8n se comunica con PostgreSQL y Redis a través de la red interna `cj_network`.
- Expone el puerto `5678` para acceso web y webhooks.

---

## 7. Preparación para producción

| Aspecto | Estado actual | Recomendación para producción |
|---------|---------------|-------------------------------|
| Base de datos | ✅ PostgreSQL | Mantener PostgreSQL. Considerar backups automáticos. |
| Autenticación | ✅ Básica activa | Migrar a autenticación más robusta si es posible (OAuth, LDAP). |
| Encriptación | ✅ Configurada | Usar clave de 32+ caracteres generada aleatoriamente. |
| Credenciales | ✅ En `.env` | Nunca hardcodear. Rotar periódicamente. |
| Persistencia | ✅ Volumen externo | Mantener `runtime/n8n` respaldado. |
| Python task runner | ⚠️ Modo interno | Considerar configurar external mode para producción. |
| HTTPS | ❌ No configurado | Configurar HTTPS y dominio propio en producción. |
| Límites de recursos | ❌ No configurados | Definir límites de CPU y memoria en `docker-compose.yml`. |

---

## 8. Beneficios de esta separación

- **Mantenimiento:** el Core puede evolucionar sin depender de la versión de n8n.
- **Escalabilidad:** es posible reemplazar n8n por otro orquestador sin reescribir la lógica de negocio.
- **Pruebas:** los workflows de n8n pueden probarse con mocks del Core.
- **Seguridad:** el acceso a datos sensibles queda centralizado en el Core.
- **Auditoría:** toda decisión importante queda registrada en el Core, no solo en logs de n8n.
