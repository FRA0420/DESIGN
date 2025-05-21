from indirizzo import Indirizzo

class Dipartimento:
    _nome:str
    _indirizzo:Indirizzo
    def __init__(self,nome:str,via:str,civico:str):
        self.setNome(nome)
        self._indirizzo=Indirizzo(via,civico)


    def setNome(self,nome:str):
        self._nome=nome

    def nome(self):
        return self._nome