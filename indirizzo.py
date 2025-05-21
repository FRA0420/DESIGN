from typing import Any
import re

class Indirizzo:
    _via:str
    _civico:str

    def __init__(self,via:str,civico:str):

        self.setVia(via)
        self.setCivico(civico)

        
    def setVia(self,via:str):

        if via is None:
            raise ValueError("via cannot be None")
        
        self._via=via

    def setCivico(self,civico:str):
        self._civico=civico

        # if civico is None:
        #     raise ValueError("civ cannot be None")

        # if civico is re.search("^[0-9]+[a-zA-Z]*$",civico):
        #     self._civico=civico
        # else:
        #     raise ValueError("civ not valido")

    def setIndirizzo(self):
        self._address= self._civico+self._via  

    def address(self):
        return self._address      

    def via(self):
        return self._via
    
    def civico(self):
        return self._civico
    
    def __hash__(self):
        return hash( (self.via(), self.civico()))
    
    def __eq__(self,other:Any):
        if other is None or not isinstance(other,type(self)) or hash(self) != hash(other):
            return False
        else:
            return (self.via(),self.civico()==(other.via(),other.civico()))
        
