import re

class Matricola:

    def __init__(self,matricola:str):
        self.setMatricolaSapienza(matricola)

    def setMatricolaSapienza(self,matr:str):
        if re.match(r"^[0-9]{7}$",matr):
            self.matr=matr
        else:
            raise ValueError("Matricola Sapienza non riconosciuta")
        
    def getMatricola(self):
        return self.matr
    
    def __hash__(self)->int:
        return hash(self.getMatricola())

    def __eq__(self,other):
        if  other is None or not isinstance(other,type(self)) or hash(self) != hash(other):
            return False
        else:
            print("Errore, non ci possono essere due alunni con la stessa matricola Sapienza")
            #si può migliorare e creare un metodo per determinare che due matricole 
            #di università diverse possono essere uguali

m=Matricola("1815865")
print(m.getMatricola())