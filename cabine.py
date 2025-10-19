class Cabine:
    def __init__(self,cod_c,letti,ponte,prezzo_base):
        self.cod_c = cod_c
        self.letti = letti
        self.ponte = ponte
        self.prezzo_base = prezzo_base
        self.disponibile=True
    @ property
    def prezzo_finale(self):
        return self.prezzo_base
    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Occupata"
        return f'{self.cod_c}, {self.letti}, {self.ponte}, {self.prezzo_finale},{stato}'
class Deluxe(Cabine):
    def __init__(self,cod_c,letti,ponte,prezzo_base,tipo):
        super().__init__(cod_c,letti,ponte,prezzo_base)
        self.tipo=tipo
    @property
    def prezzo_finale(self):
        return self.prezzo_base*1.20
    def __str__(self):
        return f"{super().__str__()}, {self.tipo}"
class CabineAnimali(Cabine):
    def __init__(self,cod_c,letti,ponte,prezzo_base,num_a):
        super().__init__(cod_c,letti,ponte,prezzo_base)
        self.num_a=num_a
    @property
    def prezzo_finale(self):
        return self.prezzo_base*(1+0.10*self.num_a)
    def __str__(self):
        return f"{super().__str__()}, {self.num_a}"