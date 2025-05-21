from telefono import Telefono,Email
from indirizzo import *

class Fornitore:

    _ragione_sociale:str
    _telefono:set[Telefono]
    _email:set[Email]
    _indirizzo:Indirizzo

    def __init__(self,ragione_sociale:str,telefono:Telefono,email:Email,via:str,civico:str):
        self.setRagioneSoc(ragione_sociale)
        self._email=Email(email)
        self._telefono=Telefono(telefono)
        self._indirizzo=Indirizzo(via,civico)
        
      

    def setRagioneSoc(self,ragione_sociale:str):
        self._ragione_sociale=ragione_sociale
    def ragionesociale(self):
        return self._ragione_sociale
    
    def add_telefono(self,telefono:Telefono):
        self._telefono.add(telefono)
    def remove_telefono(self,telefono:Telefono):
        self._telefono.remove(telefono)

    def add_email(self,email:Email):
        self._email.add(email)
    def remove_email(self,email:Email):
        self._email.remove(email)

    def telefono(self):
        return set(self._telefono)
    def email(self):
        return set(self._email)
    

fornitore1=Fornitore("disj","3478311293","chiaraciao@gmail.com","Comano","95A")
    


    

    
    
    
    
