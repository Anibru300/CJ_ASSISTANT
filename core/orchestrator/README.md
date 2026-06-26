# Core / Orchestrator

## Propósito

Configuración base y workflows fundamentales para **n8n**, el orquestador de CJ_OS.

## Responsabilidades

- Almacenar configuración base de n8n.
- Definir workflows transversales que coordinan el flujo entre conectores, Core, IA y base de datos.
- No contener lógica de negocio compleja; n8n delega la toma de decisiones al Core y a los agentes.
- Servir como capa de integración entre los eventos entrantes y el procesamiento inteligente.

## Principio arquitectónico

> **n8n es el orquestador. CJ_OS es el cerebro.**

n8n se encarga de mover datos y disparar acciones. El Core se encarga de gobernar, decidir y persistir.

## Estado

- Fase M1.2.5: estructura y documentación listas.
