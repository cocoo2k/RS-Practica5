class Task:
    def __init__(self, id: int, titol: str, assignatura: str,
                 estat: str = "pendent") -> None:
        self.id = id
        self.titol = titol
        self.assignatura = assignatura
        self.estat = estat

    def a_diccionari(self) -> dict:
        return {
            "id": self.id,
            "titol": self.titol,
            "assignatura": self.assignatura,
            "estat": self.estat,
        }

    @classmethod
    def des_de_diccionari(cls, dades: dict) -> "Task":
        return cls(
            id=dades["id"],
            titol=dades["titol"],
            assignatura=dades["assignatura"],
            estat=dades["estat"],
        )
