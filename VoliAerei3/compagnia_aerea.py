from intG1900 import intG1900
from citta import City

class CompagniaAerea:

    _nome:str #<<imm>> noto alla nascita
    _anno_fondazione:intG1900 #noto alla nascita
    _comp_direzione_citta: City    #noto alla nascita
    
    def __init__(self,nome:str,anno_fondazione:intG1900, citta_sede:City):
        self._nome=nome
        self.setAnno(anno_fondazione)
        self.set_citta_sede(citta_sede)

    def setAnno(self,anno_fondazione:intG1900) -> None:
            self._anno_fondazione=intG1900(anno_fondazione)

    
        
    def getAnno(self) -> intG1900:
        return self._anno_fondazione
    
    def getNome(self) -> str:
        return self._nome
    
    def __repr__(self) -> str:
        return f"Compagnia Aerea: {self._nome}. Fondata nel {self.getAnno()}"
    
    def citta_sede(self) -> City:
        return self._comp_direzione_citta
    
    def set_citta_sede(self,c:City) -> None:
        self._comp_direzione_citta = c
    
c = CompagniaAerea("Alitalia",1902)
print(c)
    

