class Passeggero:
    def __init__(self, codice_passegero,nome,cognome):
        self.codice_passegero=codice_passegero
        self.nome=nome
        self.cognome=cognome
    def __str__(self):
        return f' {self.codice_passegero}, {self.nome}, {self.cognome}'