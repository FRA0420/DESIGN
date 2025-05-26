class City:
    _nome:str #noto alla nascita
    _n_abitanti:int #noto alla nascita
    def __init__(self,nome:str,n_abitanti:int):
        self.setNome(nome)
        self.setAbit(n_abitanti)

    def setNome(self,nome:str):
        self._nome=nome
    def getNome(self):
        return self._nome
    
    def setAbit(self,n_abitanti):
        self._n_abitanti=n_abitanti

    def getAbit(self):
        return self._n_abitanti

    def __str__(self):
        return f"Città: {self.getNome()} con {self.getAbit()} abitanti."
