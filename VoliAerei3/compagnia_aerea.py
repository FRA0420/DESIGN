from intG1900 import intG1900

class CompagniaAerea:

    _nome:str #<<imm>> noto alla nascita
    _anno_fondazione:intG1900 #noto alla nascita
    
    def __init__(self,nome:str,anno_fondazione:intG1900):
        self._nome=nome
        self.setAnno(anno_fondazione)

   

    def setAnno(self,anno_fondazione:intG1900):
            self._anno_fondazione=intG1900(anno_fondazione)

    
        
    def getAnno(self):
        return self._anno_fondazione
    
    def getNome(self):
        return self._nome
    
    def __repr__(self):
        return f"Compagnia Aerea: {self._nome}. Fondata nel {self.getAnno()}"
    
c = CompagniaAerea("Alitalia",1902)
print(c)
    

