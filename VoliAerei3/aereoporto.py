class Aereoporto:
    _codice: str #noto alla nascita e <<imm>>
    _nome:str #noto alla nascita

    def __init__(self,codice:str,nome:str):
        self.setNome(nome)
        self._codice=codice


    def setNome(self,nome:str):
        self._nome=nome

    def getNome(self):
        return self._nome
    
    def __repr__(self):
        return f"Aereoporto nome: {self.getNome()}, codice: {self._codice}"