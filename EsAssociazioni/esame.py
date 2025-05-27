from studente import Studente
from modulo import Modulo

class esame:

    class _link:

        _studente: Studente #immutabile
        _modulo: Modulo  #immutabile
        _voto: int   #immutabile

        def __init__(self,studente:Studente, modulo: Modulo, voto:int) -> None:
            self._studente=studente
            self._modulo=modulo
            self._voto=voto

        def studente(self) -> Studente:
            return self._studente
        
        def modulo(self) -> Modulo:
            return self._modulo
        