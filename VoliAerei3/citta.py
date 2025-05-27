from TIPI import intGEZ

class City:
    _nome:str #noto alla nascita
    _n_abitanti:intGEZ #noto alla nascita
    
    
    def __init__(self,nome:str,n_abitanti:intGEZ) -> None:
        self.setNome(nome)
        self.setAbit(n_abitanti)

    def setNome(self,nome:str) -> None:
        self._nome=nome
    
    def getNome(self) -> str:
        return self._nome
    
    def setAbit(self,n_abitanti:intGEZ) -> None:
        self._n_abitanti=n_abitanti

    def getAbit(self) -> intGEZ:
        return self._n_abitanti

    def __str__(self) -> str:
        return f"Città: {self.getNome()} con {self.getAbit()} abitanti."
