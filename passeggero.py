class Passeggero:
    def __init__(self, codice_passeggero,nome,cognome):
        self.codice_passeggero=codice_passeggero
        self.nome=nome
        self.cognome=cognome
        self.cabina=None
    def assegna_cabina(self,cabina):
        self.cabina=cabina
    def __str__(self):
        return f' {self.codice_passeggero}, {self.nome}, {self.cognome}'