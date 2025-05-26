from datetime import timedelta
from intGZ import IntGZ
class Volo:
    # def __init__(self,codice:str,durata:timedelta):
    _codice:str #<<imm>>, noto alla nascita
    _durata: IntGZ #noto alla nascita
    
    def __init__(self,codice,durata):
        self._codice=codice
        self.setDurata(durata)

    def setDurata(self,durata:IntGZ):
        self._durata=IntGZ(durata)

    def durata(self):
        return self._durata
    
    def codice(self):
        return self._codice

