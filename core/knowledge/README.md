# Core / Knowledge

## Propósito

Almacenar el conocimiento estructurado de la empresa.

## Responsabilidades

- Guardar procedimientos, manuales y documentación ISO.
- Almacenar catálogos de productos, proveedores y clientes.
- Mantener información sobre cómo funciona cada área de 3P.
- Servir como base para RAG (Retrieval-Augmented Generation).
- Permitir que el Motor de IA consulte información confiable antes de responder.

## Pregunta que responde

> **¿Cómo funciona la empresa?**

## Ejemplo

- "El stock mínimo de tornillos es 100."
- "El procedimiento de compras requiere aprobación de Salvador."

## Fuentes esperadas

- `workspace/` para archivos fuente de verdad.
- PostgreSQL para referencias estructuradas.
- Vectores/embeddings para búsqueda semántica.

## Estado

- Fase M2.1: estructura y documentación listas.
