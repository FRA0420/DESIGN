from datetime import timedelta
from intGZ import IntGZ
class Volo:
    # def __init__(self,codice:str,durata:timedelta):
    _codice:str #<<imm>>, noto alla nascita
    _durata_minuti: IntGZ #noto alla nascita
    
    def __init__(self,codice:str,durata:IntGZ):
        self._codice=codice
        self.setDurata_minuti(durata)

    def setDurata_minuti(self,durata:IntGZ) -> None:
        self._durata_minuti=IntGZ(durata)

    def Getdurata_minuti(self) -> IntGZ:
        return self._durata_minuti
    
    def durata(self) -> timedelta:
        return timedelta(minutes=self._durata_minuti())
    
    def codice(self) -> str:
        return self._codice

