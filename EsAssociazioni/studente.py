from esame import *
from modulo import Modulo

class Studente:
    _nome:str
    # _esame: esame._link   #questo se ci fosse un solo esame
    _esami: dict[Modulo,esame._link]  # certamente non noto alla nascita

    def __init__(self,nome:str)->None:
        self._nome=nome
        self._esami = dict()

    def nome(self) -> str:
        return self._nome
    
    def esami(self) -> frozenset[esame._link]:
        return frozenset(self._esami.values())
    
    def add_esame(self,modulo:Modulo,voto:int)-> None:
        if modulo in self._esami:
            raise ValueError(f"Lo studente aveva già superato l'esame del modulo {modulo}")
        
        l: esame._link = esame._link(studente=self,modulo=modulo,voto=voto)

        self._esami[modulo] = l