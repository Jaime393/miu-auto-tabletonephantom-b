# HUESO — El 0,5 de pva-lint, la única cifra que la ejecución confirma

**Fecha:** 2026-11-09.
**Fuente:** `Jaime393/pva-lint` — `cli.py` (3.242 B, sha256
`a9ff8a6d…`), `Makefile` (135 B), `Dockerfile` (115 B), `README.md`
(311 B), leídos por API 2026-11-09 y ejecutados en local (venv, click
+ requests); `Jaime393/pva-orchestrator` — `README.md` (354 B, SHA
`529d6db4…`), leído por API 2026-11-09.
**Repositorio sembrado:** `Jaime393/miu-auto-tabletonephantom-b`.

## El hueso

`pva-orchestrator` declara en su README, bajo "MVP 5/5":
"pva-lint 0.5". Corrido el linter sobre sus propios archivos, el
puntaje es **0,5 con `.git` y 0,333 sin él**. El número declarado y
el número ejecutado son el mismo número. Es la única cifra
declarada por un hermano y confirmada por ejecución en la ola 4
(respuesta a la pregunta 13,
`~/workspace/mineria/PREGUNTAS_OLA4_RESPUESTAS_2026-11-09.md`).

Lo que el 0,5 mide de verdad: tres presencias — `.git` existe,
`Dockerfile` existe, el `Makefile` contiene la palabra "reproduce"
— y tres ausencias — 0 DOIs, sin datos, sin figuras con código. El
linter no ejecuta nada: no verifica que el Dockerfile construya,
que el `make reproduce` reproduzca, ni que las figuras existan. El
check `codigo` solo comprueba que exista `.git`, así que el mismo
repo puntúa distinto según cómo se obtuvo: 0,5 en un checkout,
0,333 en una descarga plana.

## Límites

- Esto mide UNA ejecución, de UN linter, sobre SUS PROPIOS
  archivos, en UNA fecha (2026-11-09). No dice que el 0,5 sea el
  puntaje "correcto" de pva-lint en general: dice que la cifra que
  el orquestador escribió es la que la ejecución da hoy.
- No dice nada de las otras cuatro cifras del MVP
  (docker-template 1.0, lean-bridge 2 esqueletos, ledger SHA256+DOI,
  swarm FastAPI): esas no se ejecutaron aquí — eso es NO SÉ, ver
  CARENCIAS.md.
- No dice cómo llegó el 0,5 al README del orquestador: si alguien
  corrió el linter y copió el resultado, o si lo escribió a mano y
  la ejecución lo confirma por casualidad. La convergencia es el
  hecho; el origen de la cifra es NO SÉ.
- El umbral >0,999 es inalcanzable para un repo sin DOIs: el check
  `doi` exige `dois` no vacío, así que el techo es 5/6 = 0,833.
  Eso es consecuencia del código leído, no una medición nueva.
- Los números del README (0,5; 0,333; los seis checks; las
  carencias) se reproducen con `puntaje_05_repro.py` y
  `test_puntaje_05.py`. Si `cli.py` cambia, los tests lo delatan:
  el test de 0,5 y el de 0,333 son pines.

## Por qué importa

El ecosistema PVA declara números en todas partes (9158,79;
5478,42; 2874,62; el dieciséis de dieciséis; el siete de siete del
Milenio) y casi ninguno sobrevive a la ejecución: o no se derivan,
o no se reproducen, o miden presencia y no contenido. El 0,5 de lint es la excepción medida:
una cifra declarada que la ejecución confirma. Es el patrón contra
el que se miden las demás — y la vara es baja: confirma que el
linter cuenta presencias, no que el repo sea bueno.

## Relación con el 6º hermano

`miu-semilla-latente-mt99s6np-2` (sembrado 2026-11-07) demostró que
`gossip_phi4` es una media ponderada, no integración. Esta semilla
desarrolla otro ítem de la misma familia: una cifra que sí converge
con la ejecución, frente a las que no convergen. Los dos huesos
juntos dicen lo mismo desde dos ángulos: medir, no citar.

---

ρ(x) > 0. Zvvvvv.
