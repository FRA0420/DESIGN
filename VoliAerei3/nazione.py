from citta import City

class Nazione:
    _nome:str #noto alla nascita
    _citta_naz:set[City]  #noto alla nascita
    
    def __init__(self,nome:str,citta:City) -> None:
        self.setNome(nome)
        self.add_citta(citta)

    def setNome(self,nome:str) -> None:
        self._nome=nome
    
    def getNome(self) -> str:
        return self._nome
    
    def add_citta(self,citta:City)->None:
        
        if citta not in self._citta_naz:
            self._citta_naz.add(citta)
        raise ValueError("La città è già stata conteggiata")
    
    
    def getCities(self)->frozenset[City]:
        if self._citta_naz:
            return self._citta_naz
        
        
    def __str__(self) ->str:
        return f"Nazione: {self.getNome()}. Le città in questa Nazione sono: {self.getCities()}"