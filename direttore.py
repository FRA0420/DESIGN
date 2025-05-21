from datetime import date
from CF import CodiceFiscale

class Direttore:
    _nome:str
    _cognome:str
    _data_nascita:str
    _anni_servizio:int
    _cf:CodiceFiscale

    def __init__(self,nome:str,cognome:str,data_nascita:date,anni_servizio:str,cf:CodiceFiscale):

        self.set_nome(nome)
        self.set_cognome(cognome)
        self.set_anni_servizio(anni_servizio)
        self.set_data_nascita(data_nascita)
        self._cf.set_cf(cf)

    
    
    def set_nome(self,nome:str):
        self._nome:str=nome
    def set_cognome(self,cognome:str):
        self._cognome=cognome
    def set_data_nascita(self,data_nascita:date):
        self._data_nascita=data_nascita
    def set_anni_servizio(self,anni_servizio:int):
        try:    
            anni_servizio >= 0
        except:
            "Errore"
        finally:
            self._anni_servizio=anni_servizio

    def nome(self)->str:
        return self._nome
    def cognome(self)->str:
        return self._cognome
    def dataNascita(self)->date:
        return self._data_nascita
    def anniServizio(self)->int:
        return self._anni_servizio
    





    


        


        

    