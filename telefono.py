import re

class Telefono:
    _telefono:str

    def __init__(self,telefono:str):
        self.setTelefono(telefono)
    
    def setTelefono(self,telefono:str):
        if len(telefono)!=10:
            raise ValueError("Inserisci numero valido")
        
        else:
            self._telefono=telefono

    def telefono(self):
        return self._telefono
    
class Email:
    _email=str

    def __init__(self,email:str):
        self.setEmail(email)

    def setEmail(self,email:str):
        if email == re.search(r'^[\w.]+\@[\w.]+$', email):
            self._email=email  
        else:
            print("Errore inserisci email valida")

    def email(self):
        return self._email

    


    