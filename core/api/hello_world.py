#!/usr/bin/env python3
"""
Hello World end-to-end de CJ_OS.

Propósito:
    Validar que n8n puede comunicarse con el Core de CJ_OS.
    Expone un endpoint HTTP simple /hello que responde con un JSON.

Uso:
    python core/api/hello_world.py

n8n lo invocará mediante un nodo HTTP Request a:
    http://host.docker.internal:8000/hello

o, si n8n corre fuera de Docker:
    http://localhost:8000/hello
"""

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

DEFAULT_PORT = 8000


class HelloWorldHandler(BaseHTTPRequestHandler):
    """Handler minimalista para el endpoint /hello."""

    def _send_json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        # CORS básico para permitir llamadas desde n8n o navegador durante pruebas.
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        if self.path == "/hello":
            self._send_json(
                200,
                {
                    "status": "ok",
                    "message": "Hola desde el Core de CJ_OS",
                    "version": "0.0.18",
                    "component": "core/api/hello_world.py",
                },
            )
        else:
            self._send_json(404, {"status": "error", "message": "Ruta no encontrada"})

    def do_POST(self) -> None:  # noqa: N802
        if self.path == "/hello":
            content_length = int(self.headers.get("Content-Length", 0))
            raw_body = self.rfile.read(content_length) if content_length else b"{}"
            try:
                body = json.loads(raw_body.decode("utf-8")) if raw_body else {}
            except json.JSONDecodeError:
                body = {"raw": raw_body.decode("utf-8", errors="replace")}

            name = body.get("name", "mundo")
            self._send_json(
                200,
                {
                    "status": "ok",
                    "message": f"Hola, {name}, desde el Core de CJ_OS",
                    "received": body,
                    "version": "0.0.18",
                    "component": "core/api/hello_world.py",
                },
            )
        else:
            self._send_json(404, {"status": "error", "message": "Ruta no encontrada"})

    def log_message(self, fmt: str, *args) -> None:  # noqa: WPS125
        # Silencia los logs estándar para no saturar la consola durante pruebas.
        pass


def main() -> None:
    port = int(os.environ.get("HELLO_WORLD_PORT", DEFAULT_PORT))
    server = HTTPServer(("0.0.0.0", port), HelloWorldHandler)
    print(f"[CJ_OS Hello World] Servidor escuchando en http://0.0.0.0:{port}/hello")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[CJ_OS Hello World] Servidor detenido.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
