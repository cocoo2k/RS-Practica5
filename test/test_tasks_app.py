import json
import subprocess
import sys
from pathlib import Path

RUTA_SCRIPT = Path(__file__).resolve().parent.parent / "src" / "tasks_app.py"


def executar_cli(
    directori: Path, *arguments: str
) -> subprocess.CompletedProcess:
    resultat = subprocess.run(
        [sys.executable, str(RUTA_SCRIPT), *arguments],
        cwd=directori,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    assert resultat.returncode == 0, resultat.stderr
    return resultat


def llegir_registres(directori: Path) -> list[dict]:
    fitxer = directori / "data" / "tasks.json"
    return json.loads(fitxer.read_text(encoding="utf-8"))


def test_gs01_creacio_tasca(tmp_path: Path) -> None:
    resultat = executar_cli(
        tmp_path, "add", "--title", "Pràctica 1", "--subject", "RS"
    )

    assert resultat.stdout == "Tasca [ID: 1] creada amb èxit\n"
    assert llegir_registres(tmp_path) == [
        {
            "id": 1,
            "titol": "Pràctica 1",
            "assignatura": "RS",
            "estat": "pendent",
        }
    ]


def test_gs02_registre_buit(tmp_path: Path) -> None:
    resultat = executar_cli(tmp_path, "list")

    assert resultat.stdout == "Registre de tasques buit.\n"
    assert llegir_registres(tmp_path) == []


def test_gs03_llistat_amb_tasques(tmp_path: Path) -> None:
    fitxer = tmp_path / "data" / "tasks.json"
    fitxer.parent.mkdir(parents=True, exist_ok=True)
    fitxer.write_text(
        json.dumps(
            [
                {
                    "id": 1,
                    "titol": "Pràctica 1",
                    "assignatura": "RS",
                    "estat": "pendent",
                },
                {
                    "id": 2,
                    "titol": "Examen parcial",
                    "assignatura": "SO",
                    "estat": "pendent",
                },
            ],
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    resultat = executar_cli(tmp_path, "list")

    assert resultat.stdout == (
        "[1] Pràctica 1 (RS) - estat: pendent\n"
        "[2] Examen parcial (SO) - estat: pendent\n"
    )
