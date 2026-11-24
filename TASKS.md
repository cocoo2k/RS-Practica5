# TASKS.md - Tasks_app

Estats: `[ ]` pendent · `[/]` en procés · `[x]` completada. Una tasca per torn; commit després de cada una.

## Increment 1: MVP - Creació i Llistat de Tasques
Objectiu: Tenir una versió CLI funcional per afegir i consultar tasques en JSON.

- [ ] Tasca 1.1: Crear estructura de directoris (`src/`, `test/`, `data/`) i fitxer `data/tasks.json` inicial. (RF-01, RF-02)
- [ ] Tasca 1.2: Implementar model de dades `Task` a `src/models.py` amb mètodes de serialització JSON.
- [ ] Tasca 1.3: Desenvolupar Tasks_app a `src/tasks_app.py` amb opcions `add` i `list`. (RF-03, RF-04)
- [ ] Tasca 1.4: Crear test d'integració a `test/test_tasks_app.py` segons GS-01, GS-02 i GS-03.
- [ ] Tasca 1.5: Validar execució amb OpenCode i verificar que tots els tests passen (`python3 -m pytest test`).

## Increment 2: Data límit, edició, completar i indicadors
Objectiu: Gestionar dates límit i el cicle de vida d'una tasca. Depèn de l'Increment 1.

- [ ] Tasca 2.1: Afegir el camp opcional `data_limit` al model `Task` i a la serialització JSON (compatible amb tasques sense el camp). (Model de dades)
- [ ] Tasca 2.2: Crear a `src/` una funció de validació de dates `YYYY-MM-DD` i una funció `data_actual()` que llegeixi `TASKS_APP_AVUI`. (RF-06)
- [ ] Tasca 2.3: Ampliar `add` amb l'opció `--due` i la validació d'errors. (RF-05, RF-06)
- [ ] Tasca 2.4: Test d'`add --due` vàlid i invàlid segons GS-04, GS-05 i GS-06.
- [ ] Tasca 2.5: Mostrar la data límit al llistat `list`. (RF-07, RF-08)
- [ ] Tasca 2.6: Implementar el comandament `done --id`. (RF-14, RF-15, RF-10)
- [ ] Tasca 2.7: Test de `done` segons GS-12 i GS-13.
- [ ] Tasca 2.8: Implementar el comandament `edit --id` amb `--title`, `--subject`, `--due` i `--status`. (RF-09, RF-10, RF-11, RF-12, RF-13)
- [ ] Tasca 2.9: Test d'`edit` segons GS-07, GS-08, GS-09, GS-10 i GS-11.
- [ ] Tasca 2.10: Afegir els indicadors `[CADUCADA]` i `[URGENT]` al llistat. (RF-16)
- [ ] Tasca 2.11: Test dels indicadors segons GS-14, GS-15, GS-16 i GS-17.
- [ ] Tasca 2.12: Executar `python3 -m pytest test` i verificar que tots els tests (Increments 1 i 2) passen.

