class Cabine:
    def __init__(self,cod_c,letti,ponte,prezzo_base):
        self.cod_c = cod_c
        self.letti = letti
        self.ponte = ponte
        self.prezzo_base = prezzo_base
    def __str__(self):
        return f'{self.cod_c}, {self.letti}, {self.ponte}, {self.prezzo_base}'
class Deluxe(Cabine):
    def __init__(self,cod_c,letti,ponte,prezzo_base,tipo):
        super().__init__(cod_c,letti,ponte,prezzo_base)
        self.tipo=tipo
    @property
    def sovraprezzo(self):
        self.prezzo_base =self.prezzo_base*1.20
        return self.prezzo_base
class CabineAnimali(Cabine):
    def __init__(self,cod_c,letti,ponte,prezzo_base,num_a):
        super().__init__(cod_c,letti,ponte,prezzo_base)
        self.num_a=num_a
    @property
    def sovraprezzo(self):
        self.prezzo_base =self.prezzo_base*(1+0.10*self.num_a)
        return self.prezzo_base