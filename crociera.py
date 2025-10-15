import csv
from cabine import *

from passeggero import Passeggero
class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome=nome
        self.passeggeri=[]
        self.cabine=[]

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        f=open(file_path,'r')
        righe=csv.reader(f)
        for riga in righe:
            if len(riga)==3:
                p=Passeggero(riga[0],riga[1],riga[2])
                self.passeggeri.append(p)
                return p
            if len(riga)==4:
                cabina=Cabine(riga[0],riga[1],riga[2],int(riga[3]))
                self.cabine.append(cabina)
                return cabina
            if len(riga)==5:
                if riga[4].isdigit():
                    ca=CabineAnimali(riga[0],riga[1],riga[2],int(riga[3]),int(riga[4]))
                    ca.sovraprezzo()
                    self.cabine.append(ca)
                    return ca
                else:
                    cd=Deluxe(riga[0],riga[1],riga[2],int(riga[3]),riga[4])
                    cd.sovraprezzo()
                    self.cabine.append(cd)
                    return cd




    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

