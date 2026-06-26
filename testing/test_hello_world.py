#!/usr/bin/env python3
"""
Pruebas básicas para el Hello World de CJ_OS.

Uso:
    python testing/test_hello_world.py
"""

import json
import subprocess
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


class TestHelloWorldCLI(unittest.TestCase):
    """Pruebas para la versión CLI del Hello World."""

    def _run_cli(self, *extra_args: str) -> dict:
        cmd = [sys.executable, str(PROJECT_ROOT / "core" / "hello_world_cli.py"), *extra_args]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)

    def test_default_salutation(self):
        response = self._run_cli()
        self.assertEqual(response["status"], "ok")
        self.assertIn("mundo", response["message"])

    def test_custom_name(self):
        response = self._run_cli("--name", "Francisco")
        self.assertEqual(response["status"], "ok")
        self.assertIn("Francisco", response["message"])


class TestHelloWorldHTTPServer(unittest.TestCase):
    """Pruebas para la versión HTTP del Hello World."""

    def test_module_imports(self):
        # Verifica que el módulo del servidor se pueda importar sin errores.
        import core.api.hello_world as hw  # noqa: F401

        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
