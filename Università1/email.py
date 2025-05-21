import re
from typing import Any

class Email:
    _email=str

    def __init__(self,mail:str):
        self.setEmail(mail)

    def setEmail(self,email:str):
        if re.findall(r"^\S+@\S+\.\S+$", email):
            self._email=email
        else:
            raise ValueError("Errore email non valida ") 


    def email(self):
        return self._email
    
    def __hash__(self):
        return hash(self.email())
    
    def __eq__(self,other:Any):
        if other is None or other is not isinstance(other,type(self)) or hash(self) != hash(other):
            return False
        return self.email() == other.email()
    
e=Email("chiara.macciocchi17@gmail.com")
print(e.email())


