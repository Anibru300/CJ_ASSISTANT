#!/usr/bin/env python3
"""
Hello World CLI de CJ_OS.

Propósito:
    Versión por línea de comandos del Hello World para ser invocada
    directamente desde n8n mediante un nodo "Execute Command".

Uso:
    python core/hello_world_cli.py
    python core/hello_world_cli.py --name Francisco

n8n puede ejecutar:
    python /c/Projects/CJ_Assistant/core/hello_world_cli.py --name "{{ $json.name }}"
"""

import argparse
import json
import sys


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Hello World de CJ_OS")
    parser.add_argument(
        "--name",
        default="mundo",
        help="Nombre a incluir en el saludo (default: mundo).",
    )
    args = parser.parse_args(argv)

    response = {
        "status": "ok",
        "message": f"Hola, {args.name}, desde el Core de CJ_OS",
        "version": "0.0.18",
        "component": "core/hello_world_cli.py",
    }
    print(json.dumps(response, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
