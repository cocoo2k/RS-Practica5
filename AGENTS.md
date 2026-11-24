# AGENTS.md — Directives per a OpenCode

## Entorn i Stack Tècnic
- Llenguatge: Python 3.11+
- Interfície: Línia de comandes (CLI) amb mòdul `argparse` o `cmd`
- Manteniment de Dades: Fitxer JSON local (`data/tasks.json`)
- Tests: `pytest` (única dependència externa autoritzada)

## Comandes de Desenvolupament
- Executar aplicació: `python3 src/tasks_app.py <comanda>` (ex. `python3 src/tasks_app.py list`)
- Executar tots els tests: `python3 -m pytest test`
- Executar test únic: `python3 -m pytest test/test_task.py`

## Convencions de Codi
- Estil: PEP8.
- Idioma del codi i comentaris: Català (mantenir consistència en noms de variables).
- Els missatges per pantalla han de coincidir literalment amb els de `SPECIFICATIONS.md`.
- Data actual: llegir-la de la variable d'entorn `TASKS_APP_AVUI` (format `YYYY-MM-DD`);
  si no existeix, usar la data del sistema. Els tests han de fixar `TASKS_APP_AVUI`.
- Format de dates: `YYYY-MM-DD` (ISO 8601).

## Regles de Gestió de Tasques (`TASKS.md`)
1. Llegeix `TASKS.md` i identifica la següent tasca amb estat `[ ]`.
2. Canvia l'estat de la tasca actual a `[/]` abans d'iniciar la codificació.
3. Executa ÚNICAMENT una sola tasca per torn.
4. Verifica que el codi compleixi els requisits i escenaris Gherkin de `SPECIFICATIONS.md`.
5. Quan estigui completada i verificada, canvia l'estat a `[x]`.
6. Atura't i demana confirmació a l'usuari abans de passar a la següent tasca.
7. Si un test falla, intenta corregir-lo com a màxim 3 vegades; després atura't i informa.

## Restriccions de Desenvolupament
- No instal·lis llibreries externes no autoritzades.
- No modifiquis fitxers de configuració fora de `src/` i `test/`.
- Només pots escriure a `src/`, `test/`, `data/tasks.json` i `TASKS.md`.
- Mai modifiquis `SPECIFICATIONS.md` ni `AGENTS.md`: si hi trobes una ambigüitat, pregunta.
- Mai implementis funcionalitats que no estiguin a `SPECIFICATIONS.md`.
- Mai facis `git commit` ni `git push`: ho fa l'usuari.
- Mai esborris `data/tasks.json` ni en canviïs el format de les tasques ja existents.
