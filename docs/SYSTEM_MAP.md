# Mapa del Sistema CJ_OS

**Versión:** 0.2.0  
**Fecha:** 2026-06-25  
**Estado:** Documento visual de referencia rápida. Fuente maestra: `docs/CJ_OS_BLUEPRINT.md`.

> Este documento es **exclusivamente visual**. Para detalles de arquitectura, dominios, filosofía y decisiones, consultar:
> - `docs/CJ_OS_BLUEPRINT.md`
> - `docs/CJ_OS_PHILOSOPHY.md`
> - `docs/CJ_OS_OPERATING_MODEL.md`
> - `docs/DECISIONS.md`
> - `docs/ROADMAP.md`

---

## Vista general de componentes

```text
                         Usuarios / Canales externos
    Carlos    WhatsApp    Outlook    Web/Dashboard    OneDrive/Google/SAE/Excel
       │          │           │             │                      │
       └──────────┴───────────┴─────────────┴──────────────────────┘
                                     │
                                     ▼
                         ┌─────────────────────┐
                         │   Event Bus / Queue │
                         │      (Redis)        │
                         └──────────┬──────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
 ┌─────────────┐          ┌─────────────────┐          ┌──────────────────┐
 │  Scheduler  │          │ Orchestrator    │          │ Core — Cerebro   │
 │  (tareas    │          │ (n8n workflows) │          │                  │
 │ recurrentes)│          └────────┬────────┘          │ ├─ events        │
 └─────────────┘                   │                   │ ├─ scheduler     │
                                   │                   │ ├─ audit         │
        ┌──────────────────────────┼───────────────────┤ ├─ security      │
        │                          │                   │ ├─ config        │
        ▼                          ▼                   │ ├─ api           │
 ┌─────────────┐          ┌──────────────┐             │ ├─ orchestrator  │
 │  Connectors │          │    Agents    │             │ ├─ memory        │
 │  whatsapp   │          │  Almacén     │             │ ├─ knowledge     │
 │  onedrive   │          │  Calidad     │             │ ├─ rules         │
 │  google     │          │  Ventas      │             │ ├─ goals         │
 │  outlook    │          │  Compras     │             │ ├─ behavior      │
 │  sae        │          │  RRHH        │             │ ├─ decision_engine│
 │  excel      │          │  Logística   │             │ ├─ reasoning     │
 └──────┬──────┘          │  Gerencia    │             │ └─ policies      │
        │                 │  SGC         │             └────────┬─────────┘
        │                 └──────┬───────┘                      │
        │                        │                              │
        └────────────────────────┼──────────────────────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │        AI Layer         │
                    │  providers / prompts    │
                    │  memory / agents / tools│
                    └────────────┬────────────┘
                                 │
                                 ▼
              ┌─────────────────────────────────────┐
              │         Fuentes de verdad           │
              │  PostgreSQL  │  Redis  │  Workspace │
              │  (datos)     │  (colas)│  (archivos)│
              └─────────────────────────────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     Runtime / Backups   │
                    │  logs / temp / cache    │
                    └─────────────────────────┘
```

---

## Cinco capas de inteligencia del Core

```text
         ┌─────────────────┐
         │   Behavior      │  ← ¿Cómo debe comportarse? (ADN / Constitución)
         ├─────────────────┤
         │     Goals       │  ← ¿Qué se intenta lograr?
         ├─────────────────┤
         │     Rules       │  ← ¿Qué está permitido?
         ├─────────────────┤
         │   Knowledge     │  ← ¿Cómo funciona la empresa?
         ├─────────────────┤
         │    Memory       │  ← ¿Qué pasó?
         └─────────────────┘
```

---

## Flujo de decisión simplificado

```text
Evento entrante
      │
      ▼
┌─────────────┐
│   Memory    │ ¿Ya pasó algo similar?
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Knowledge  │ ¿Cómo se resuelve esto en 3P?
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Rules    │ ¿Está permitido?
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Goals    │ ¿Alinea con el objetivo?
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Behavior   │ ¿Cómo responde CJ_OS según su ADN?
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│ Decision Engine │
│  ├─ Actuar      │
│  ├─ Proponer    │
│  ├─ Confirmar   │
│  └─ Escalar     │
└─────────────────┘
```

---

## Leyenda

| Símbolo | Significado |
|---------|-------------|
| **Event Bus / Queue** | Cola central de eventos, implementada sobre Redis. |
| **Orchestrator (n8n)** | Motor de workflows; mueve datos y dispara acciones. |
| **Core** | Cerebro del sistema: eventos, scheduler, auditoría, seguridad, configuración, memoria, conocimiento, reglas, objetivos, comportamiento, motor de decisiones, razonamiento y políticas. |
| **Agents** | Agentes de IA especializados por área de negocio. |
| **Connectors** | Conectores con sistemas externos. |
| **AI Layer** | Proveedores, prompts, memoria conversacional, agentes y herramientas. |
| **Workspace** | Archivos fuente de verdad (PDFs, Excel, imágenes, Word). |
| **Runtime** | Logs, temporales, caché, base de datos y respaldos. |
