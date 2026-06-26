# Core / Decision Engine

## Propósito

El Motor de Decisiones es el corazón de CJ_OS. No es un LLM. Es el componente que decide qué acción tomar ante cada evento, basándose en memoria, conocimiento, reglas, objetivos y políticas.

## Responsabilidades

- Clasificar eventos entrantes.
- Evaluar contexto, reglas, objetivos y políticas.
- Decidir si actúa automáticamente, pide confirmación o escala a un humano.
- Seleccionar el agente especializado adecuado del Consejo de Agentes.
- Registrar la cadena de decisión en auditoría.
- Garantizar que CJ_OS no responda "guardo la foto" sin antes entender qué hacer con ella.

## Ejemplo de decisión

> Francisco manda una foto.

El Motor de Decisiones se pregunta:

- ¿Qué recibí?
- ¿A quién pertenece?
- ¿Es evidencia, catálogo, factura o foto de almacén?
- ¿Debe ir a Drive, OneDrive o crear una tarea?
- ¿Debe avisar a Carlos o ignorarse?

## Estado

- Fase M2.2: estructura y documentación listas.
