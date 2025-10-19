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
            if len(riga)==4:
                cabina=Cabine(riga[0],riga[1],riga[2],int(riga[3]))
                self.cabine.append(cabina)
            if len(riga)==5:
                if riga[4].isdigit():
                    ca=CabineAnimali(riga[0],riga[1],riga[2],float(riga[3]),float(riga[4]))
                    _=ca.prezzo_finale
                    self.cabine.append(ca)
                else:
                    cd=Deluxe(riga[0],riga[1],riga[2],float(riga[3]),riga[4])
                    _ =cd.prezzo_finale
                    self.cabine.append(cd)
        for c in self.cabine:
            print(c)
        for p in self.passeggeri:
            print(p)



    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        passeggero_trovato = None
        cabina_trovata = None

        for p in self.passeggeri:
            if p.codice_passeggero == codice_passeggero:
                passeggero_trovato = p
                break

        if passeggero_trovato is None:
            raise Exception('Passeggero non trovato')

        if passeggero_trovato.cabina is not None and passeggero_trovato.cabina is not None:
            raise Exception('Passeggero già assegnato a un’altra cabina')
        for c in self.cabine:
            if c.cod_c == codice_cabina:
                cabina_trovata = c
                break

        if cabina_trovata is None:
            raise Exception('Cabina non trovata')

        if cabina_trovata.disponibile == False:
            raise Exception('Cabina già occupata')

        passeggero_trovato.assegna_cabina(cabina_trovata)
        cabina_trovata.disponibile = False

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

