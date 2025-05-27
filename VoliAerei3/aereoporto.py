class Aereoporto:
    _codice: str #noto alla nascita e <<imm>>
    _nome:str #noto alla nascita

    def __init__(self,codice:str,nome:str):
        self.setNome(nome)
        self._codice=codice


    def setNome(self,nome:str) -> None:
        self._nome=nome

    def getNome(self) -> str:
        return self._nome
    
    def getCodice(self) -> str:
        return self._codice
    
    def __repr__(self) -> str:
        return f"Aereoporto nome: {self.getNome()}, codice: {self.getNome()}"