#!/usr/bin/env python3
"""Tests del puntaje 0,5 de pva-lint — miu-auto-tabletonephantom-b.

Reproducen cada número del hecho medido con la copia fiel de
`scan_repo` de `puntaje_05_repro.py`. Solo stdlib, solo lectura local,
sin red. Correr: python3 test_puntaje_05.py
"""

import hashlib
import unittest

from puntaje_05_repro import (
    DOCKERFILE,
    MAKEFILE,
    README_MD,
    _fixture,
    scan_repo,
)

# La cita declarada por el hermano: el bloque MVP del README de
# pva-orchestrator (Jaime393/pva-orchestrator — README.md, 354 B,
# sha256 529d6db42e282bde2f0bcbd1b4b3aa5f7905cfa5, leído por API
# 2026-11-09). Texto literal, no resumen.
MVP_ORQUESTADOR = """MVP 5/5:
- pva-lint 0.5
- pva-docker-template 1.0
- pva-lean-bridge 2 esqueletos
- pva-ledger SHA256+DOI
- pva-swarm FastAPI"""


class TestPuntaje05(unittest.TestCase):
    def test_con_git_da_0_5(self):
        r = scan_repo(_fixture(True))
        self.assertEqual(r["pva_score"], 0.5)

    def test_sin_git_da_0_333(self):
        r = scan_repo(_fixture(False))
        self.assertEqual(r["pva_score"], 0.333)

    def test_checks_con_git(self):
        r = scan_repo(_fixture(True))
        self.assertEqual(r["checks"], {
            "doi": "0/0 verificables",
            "datos": "faltan",
            "codigo": "repo abierto",
            "docker": "presente",
            "reproduce": "make reproduce existe",
            "figuras": "sin codigo fuente",
        })

    def test_checks_sin_git(self):
        r = scan_repo(_fixture(False))
        self.assertEqual(r["checks"]["codigo"], "no git")
        self.assertEqual(r["checks"]["docker"], "presente")
        self.assertEqual(r["checks"]["reproduce"], "make reproduce existe")

    def test_carencias_con_git(self):
        r = scan_repo(_fixture(True))
        self.assertEqual(r["carencias"], [
            "0 DOIs rotos de 0",
            "datos no publicos con DOI/URL",
            "figuras sin codigo fuente",
        ])

    def test_carencias_sin_git(self):
        r = scan_repo(_fixture(False))
        self.assertEqual(r["carencias"], [
            "0 DOIs rotos de 0",
            "datos no publicos con DOI/URL",
            "codigo no en repo abierto",
            "figuras sin codigo fuente",
        ])

    def test_el_orquestador_declara_0_5(self):
        self.assertIn("- pva-lint 0.5", MVP_ORQUESTADOR)

    def test_fixture_es_fiel(self):
        # Los archivos del fixture son byte a byte los del repo
        # (sha256 medidos al descargarlos por API 2026-11-09).
        self.assertEqual(
            hashlib.sha256(README_MD.encode()).hexdigest(),
            "75e15572154d6165c8e79b16027fe64c313ac5e9cc9a021553fd6412114b1ae2")
        self.assertEqual(
            hashlib.sha256(MAKEFILE.encode()).hexdigest(),
            "93f709140fe84786208dcbb149250fe0a761c7d54739b4267f0cb865402a473b")
        self.assertEqual(
            hashlib.sha256(DOCKERFILE.encode()).hexdigest(),
            "7da0ba72a5cb5d66c926212984a9838de764c84db595a79a39b4402ee8f8ecbe")


if __name__ == "__main__":
    unittest.main(verbosity=2)
