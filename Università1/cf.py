import re

class CodiceFiscale:
    
    def __init__(self,cf:str):
        self.set_cf(cf)
        
        
    def set_cf(self,cf:str):
        if not re.fullmatch(r"[A-Za-z0-9]{16}",cf):
            raise "cofice fiscale non valido"
        self.cf=cf

    def getCF(self):
        return self.cf
    
    def __hash__(self):
        return hash(self.getCF())
    
    def __eq__(self,other):
        if other is None or not isinstance(other,type(self)) or hash(self) != hash(other):
            return False
        return self.getCF() == other.getCF()
    
codiceficale=CodiceFiscale("MCCCHR98T57H501Q")
print(codiceficale.getCF())