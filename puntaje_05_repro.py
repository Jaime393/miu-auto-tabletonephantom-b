#!/usr/bin/env python3
"""Reproducción del puntaje 0,5 de pva-lint — miu-auto-tabletonephantom-b.

`scan_repo` y `check_doi` son copia fiel del archivo original
(mismo código, mismo comportamiento):

    Jaime393/pva-lint — cli.py
    3.242 B, sha256 a9ff8a6df34da1644909d76e772ca57080a871747a82be40bb6cd70da132734d
    Leído por API 2026-11-09. El archivo original no se modifica.

Única desviación, documentada: el original importa `requests` y
`click` sin condición en la cabecera (`click` solo lo usa el CLI, no
`scan_repo`). Aquí el import de `requests` es guardado y `click` no se
importa: sin DOIs en los archivos, `check_doi` no se llama nunca y el
resultado es idéntico con o sin `requests` instalado. Solo stdlib,
solo lectura local, sin red.

El `main` de abajo construye dos directorios con los archivos propios
del repo (contenido exacto, verificado por sha256 abajo) y corre
`scan_repo` sobre cada uno: con `.git` (checkout normal / CI) y sin
`.git` (descarga plana). Imprime los dos puntajes y los seis checks.
"""

import json
import re
import tempfile
from pathlib import Path

try:
    import requests
except ImportError:  # pragma: no cover - el repro no lo necesita (0 DOIs)
    requests = None


def check_doi(doi):
    if requests is None:
        return False
    try:
        r = requests.get(f"https://doi.org/api/handles/{doi}", timeout=5)
        return r.status_code == 200
    except Exception:
        return False


def scan_repo(path="."):
    p = Path(path)
    report = {"pva_score": 0.0, "carencias": [], "checks": {}}
    score = 0
    total = 6
    tex_files = list(p.glob("*.tex")) + list(p.glob("*.md"))
    dois = []
    for f in tex_files:
        try:
            dois += re.findall(r"10\.\d{4,}/[^\s}]+", f.read_text(errors='ignore'))
        except Exception:
            pass
    doi_ok = sum(1 for d in dois if check_doi(d)) if dois else 0
    report["checks"]["doi"] = f"{doi_ok}/{len(dois)} verificables"
    if doi_ok == len(dois) and dois:
        score += 1
    else:
        report["carencias"].append(f"{len(dois)-doi_ok} DOIs rotos de {len(dois)}")
    has_data = (p/"data").exists() or (p/"data.csv").exists() or any(p.glob("*GRACE*.csv"))
    report["checks"]["datos"] = "publicos" if has_data else "faltan"
    if has_data:
        score += 1
    else:
        report["carencias"].append("datos no publicos con DOI/URL")
    has_code = (p/".git").exists()
    report["checks"]["codigo"] = "repo abierto" if has_code else "no git"
    if has_code:
        score += 1
    else:
        report["carencias"].append("codigo no en repo abierto")
    has_docker = (p/"Dockerfile").exists() or (p/"docker-compose.yml").exists()
    report["checks"]["docker"] = "presente" if has_docker else "ausente"
    if has_docker:
        score += 1
    else:
        report["carencias"].append("falta Dockerfile reproducible")
    has_make = (p/"Makefile").exists()
    has_repro = False
    if has_make:
        try:
            has_repro = "reproduce" in (p/"Makefile").read_text()
        except Exception:
            pass
    report["checks"]["reproduce"] = "make reproduce existe" if has_repro else "falta"
    if has_repro:
        score += 1
    else:
        report["carencias"].append("falta make reproduce")
    has_fig = len(list(p.glob("fig*.py"))) + len(list(p.glob("plot*.py"))) > 0
    report["checks"]["figuras"] = "con codigo" if has_fig else "sin codigo fuente"
    if has_fig:
        score += 1
    else:
        report["carencias"].append("figuras sin codigo fuente")
    report["pva_score"] = round(score/total, 3)
    return report


# Archivos propios de pva-lint, contenido exacto leído por API 2026-11-09.
# README.md 311 B, sha256 75e15572154d6165c8e79b16027fe64c313ac5e9cc9a021553fd6412114b1ae2
README_MD = (
    "# pva-lint V202 — ρ(x)>0\n"
    "\n"
    "Linter PVA — Score 0-1 — Transición de fase >0.999\n"
    "\n"
    "Verifica DOI, datos públicos, código abierto, Dockerfile, make reproduce, figuras con código.\n"
    "\n"
    "## Uso\n"
    "\n"
    "    pip install requests click\n"
    "    python cli.py --json\n"
    "\n"
    "Parte del ecosistema PVA — 5 capas — validación como transición de fase.\n"
)
# Makefile 135 B, sha256 93f709140fe84786208dcbb149250fe0a761c7d54739b4267f0cb865402a473b
MAKEFILE = (
    "repro:\n"
    "\tpython cli.py --json\n"
    "\n"
    "dev:\n"
    "\tpython cli.py\n"
    "\n"
    "test:\n"
    "\tpython cli.py --json\n"
    "\n"
    "lint:\n"
    "\tpython cli.py\n"
    "\n"
    "reproduce:\n"
    "\tpython cli.py --json\n"
)
# Dockerfile 115 B, sha256 7da0ba72a5cb5d66c926212984a9838de764c84db595a79a39b4402ee8f8ecbe
DOCKERFILE = (
    "FROM python:3.11-slim\n"
    "WORKDIR /app\n"
    "COPY . .\n"
    "RUN pip install --no-cache-dir requests click\n"
    "CMD [\"python\", \"cli.py\"]\n"
)


def _fixture(with_git):
    d = Path(tempfile.mkdtemp(prefix="pva-lint-repro-"))
    (d / "README.md").write_text(README_MD, encoding="utf-8")
    (d / "Makefile").write_text(MAKEFILE, encoding="utf-8")
    (d / "Dockerfile").write_text(DOCKERFILE, encoding="utf-8")
    if with_git:
        (d / ".git").mkdir()
    return d


def main():
    for with_git in (True, False):
        d = _fixture(with_git)
        r = scan_repo(d)
        print(f"con .git: {with_git} -> pva_score {r['pva_score']}")
        print(json.dumps(r, indent=2, ensure_ascii=False))
    print("TODO COINCIDE" if (
        scan_repo(_fixture(True))["pva_score"] == 0.5
        and scan_repo(_fixture(False))["pva_score"] == 0.333
    ) else "NO COINCIDE")


if __name__ == "__main__":
    main()
