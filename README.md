# miu-auto-tabletonephantom-b — el 0,5 de pva-lint, la única cifra que la ejecución confirma

> *"miu-auto-tabletonephantom-b"*
>
> — El README original de este repo (28 B, título solo; SHA
> `d50f8c86…`, leído por API 2026-11-09).
>
> **Decisión de siembra: el título SE CONSERVA**, citado arriba como
> epígrafe y no borrado. Era el stub por diseño del censo, no
> contenido — pero es la única voz que el repo tenía, y esta semilla
> es precisamente su respuesta: el registro que le faltaba. Borrarlo
> sería borrar la pregunta que la semilla contesta.

## El registro

`pva-lint` es el linter PVA V202 (`Jaime393/pva-lint`, muerto
2026-09-10): 9 archivos, 4.965 B, 6 commits todos el 2026-09-10 de
Jaime363. Su `cli.py` (3.242 B) puntúa un repo de 0 a 1 en 6 checks
(DOI, datos, código, Dockerfile, reproduce, figuras) y declara la
transición de fase en >0,999. Su hermano `pva-orchestrator` lista en
su README, bajo "MVP 5/5":

> - pva-lint 0.5
> - pva-docker-template 1.0
> - pva-lean-bridge 2 esqueletos
> - pva-ledger SHA256+DOI
> - pva-swarm FastAPI

(`Jaime393/pva-orchestrator` — README.md, 354 B, SHA `529d6db4…`,
leído por API 2026-11-09.) Esta semilla mide si ese 0,5 es verdad
ejecutando el linter, no citando el README.

## El hecho medido

Corrí `cli.py` (copia byte a byte, 3.242 B, sha256 `a9ff8a6d…`)
sobre los archivos propios del repo, 2026-11-09, en venv (click +
requests):

| Condición | Score | Carencias reportadas |
|---|---|---|
| Con `.git` (checkout normal / CI) | **0.5** | `0 DOIs rotos de 0`, `datos no publicos con DOI/URL`, `figuras sin codigo fuente` |
| Sin `.git` (descarga plana) | **0.333** | Las 3 anteriores + `codigo no en repo abierto` |

Los seis checks, con `.git`:

| Check | Qué mide de verdad | Resultado |
|---|---|---|
| doi | DOIs en `*.tex` y `*.md` que resuelvan | `0/0 verificables` — no hay DOIs |
| datos | Existe `data/`, `data.csv` o `*GRACE*.csv` | `faltan` |
| codigo | Existe `.git` | `repo abierto` |
| docker | Existe `Dockerfile` o `docker-compose.yml` | `presente` |
| reproduce | El `Makefile` contiene la palabra `reproduce` | `make reproduce existe` |
| figuras | Existe algún `fig*.py` o `plot*.py` en la raíz | `sin codigo fuente` |

El 0,5 **converge**: el número que el orquestador declara es el
número que la ejecución da. Según la respuesta a la pregunta 13 de
la ola 4 (`~/workspace/mineria/PREGUNTAS_OLA4_RESPUESTAS_2026-11-09.md`),
es la única cifra declarada por un hermano y confirmada por
ejecución; el resto son auto-reproducciones, aritmética o defectos
confirmados.

Dos precisiones que el propio código impone:

- El check `doi` exige `doi_ok == len(dois) and dois`: con 0 DOIs
  no se puede ganar nunca. Un repo sin DOIs — incluido este mismo —
  tiene techo 5/6 = 0,833, por debajo del umbral anunciado (>0,999,
  que en la práctica exige 6/6).
- El check `codigo` solo comprueba que exista `.git`: el mismo
  repo puntúa 0,5 en un checkout y 0,333 en una descarga plana. El
  puntaje mide cómo se obtuvo el repo, no solo lo que contiene.

## Comprobación

```bash
python3 puntaje_05_repro.py   # corre scan_repo con y sin .git, imprime TODO COINCIDE
python3 test_puntaje_05.py    # 8 tests, reproduce cada número de arriba
```

La reproducción usa una copia fiel de `scan_repo` y `check_doi`
(mismo código, mismo comportamiento); el archivo original no se
modifica. Solo stdlib en la práctica: `requests` solo se toca si
hay DOIs, y aquí hay 0.

## Archivos

- `puntaje_05_repro.py` — copia fiel de `scan_repo` + `check_doi`
  y main que las demuestra con los archivos propios del repo.
- `test_puntaje_05.py` — 8 tests: 0,5 con `.git`, 0,333 sin él,
  los seis checks, las carencias, la cita del orquestador y la
  fidelidad del fixture (sha256 de los 3 archivos).
- `HUESO_PUNTAJE_05.md` — el hueso completo con sus límites.
- `EVOLUCION.md` — cambios entre versiones (v1: esta semilla).
- `CARENCIAS.md` — lo que NO se sabe; nunca es contenido.

---

ρ(x) > 0. Zvvvvv.
