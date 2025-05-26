class Nazione:
    _nome:str #noto alla nascita
    
    def __init__(self,nome:str):
        self.setNome(nome)

    def setNome(self,nome:str):
        self._nome=nome
    def getNome(self):
        return self._nome
    

    def __str__(self):
        return f"Nazione: {self.getNome()}"