import argparse
import json
from pathlib import Path

from models import Task

RUTA_DADES = Path("data") / "tasks.json"


def carregar_tasques() -> list[Task]:
    if not RUTA_DADES.exists():
        RUTA_DADES.parent.mkdir(parents=True, exist_ok=True)
        RUTA_DADES.write_text("[]", encoding="utf-8")
        return []
    dades = json.loads(RUTA_DADES.read_text(encoding="utf-8"))
    return [Task.des_de_diccionari(registre) for registre in dades]


def desar_tasques(tasques: list[Task]) -> None:
    RUTA_DADES.parent.mkdir(parents=True, exist_ok=True)
    dades = [tasca.a_diccionari() for tasca in tasques]
    RUTA_DADES.write_text(
        json.dumps(dades, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def afegir_tasca(titol: str, assignatura: str) -> Task:
    tasques = carregar_tasques()
    identificador = max((tasca.id for tasca in tasques), default=0) + 1
    nova_tasca = Task(identificador, titol, assignatura)
    tasques.append(nova_tasca)
    desar_tasques(tasques)
    return nova_tasca


def main() -> None:
    analitzador = argparse.ArgumentParser(
        description="Gestor de tasques acadèmiques."
    )
    subcomandes = analitzador.add_subparsers(dest="comanda", required=True)
    afegir = subcomandes.add_parser("add", help="Afegeix una nova tasca.")
    afegir.add_argument("--title", required=True, help="Títol de la tasca.")
    afegir.add_argument(
        "--subject", required=True, help="Assignatura de la tasca."
    )
    subcomandes.add_parser(
        "list", help="Mostra totes les tasques registrades."
    )
    arguments = analitzador.parse_args()

    if arguments.comanda == "add":
        tasca = afegir_tasca(arguments.title, arguments.subject)
        print(f"Tasca [ID: {tasca.id}] creada amb èxit")
    else:
        tasques = carregar_tasques()
        if not tasques:
            print("Registre de tasques buit.")
        else:
            for tasca in tasques:
                print(
                    f"[{tasca.id}] {tasca.titol} ({tasca.assignatura})"
                    f" - estat: {tasca.estat}"
                )


if __name__ == "__main__":
    main()
