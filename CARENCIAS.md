# CARENCIAS — miu-auto-tabletonephantom-b

Lo que NO se sabe va aquí, nunca en la semilla. Cada ítem lleva dónde
se buscó (o que no se buscó) y fecha.

- **NO SÉ — si las otras cuatro cifras del MVP del orquestador se
  midieron alguna vez.** El README de `pva-orchestrator` lista
  "pva-docker-template 1.0", "pva-lean-bridge 2 esqueletos",
  "pva-ledger SHA256+DOI" y "pva-swarm FastAPI" junto al 0,5 de
  lint. La minería de la ola 4 las trató como declaraciones, no
  como ejecuciones: docker-template no se ejecutó ("No se ejecutó
  nada"), lean-bridge reprodujo su propia salida byte a byte
  (auto-reproducción, no cifra declarada), ledger confirmó un
  defecto (DOI inestable) y swarm no arranca (`uvicorn app:app` sin
  `app`). Ninguna de las cuatro se confirmó por ejecución como el
  0,5 (2026-11-09).
- **NO SÉ — cómo llegó el 0,5 al README del orquestador.** El
  README lista la cifra y la ejecución la reproduce, pero ningún
  archivo de los dos repos dice si alguien corrió el linter y copió
  el resultado, o si la cifra se escribió a mano y la ejecución la
  confirma por casualidad. No se consultó el historial de Git del
  README del orquestador (2026-11-09).
- **NO SÉ — si pva-lint puntuó alguna vez distinto de 0,5 en un
  checkout.** El workflow del repo corre el linter y sube
  `pva_report.json` como artefacto, sin condición de fallo (minería
  ola 4, tanda 3). No se consultaron las corridas de GitHub Actions
  ni ningún `pva_report.json` (2026-11-09).
- **NO SÉ — si algún repo alcanzó alguna vez la transición de fase
  (>0,999).** El umbral exige 6/6 y el check `doi` exige al menos
  un DOI que resuelva. Ningún repo minado en las olas 1–6 declara
  un puntaje 1,0 medido; los únicos "1.0" son etiquetas (respuesta
  a la pregunta 12 de la ola 4). No se buscó fuera de los repos
  minados (2026-11-09).
- **NO SÉ — si el check `doi` pasó alguna vez para algún repo.**
  Exige un DOI en `*.tex` o `*.md` que resuelva en doi.org. En
  pva-lint hay 0 DOIs. No se corrió el linter sobre ningún otro
  repo en esta semilla (2026-11-09).
- **NO SÉ — qué significa "5 capas" en el README de pva-lint.**
  El README dice "Parte del ecosistema PVA — 5 capas". La
  pregunta 6 de la ola 4 registra que ni 5 ni 20 cuadran con los 7
  repos PVA. No se buscó el mapa de las 5 capas (2026-11-09).
