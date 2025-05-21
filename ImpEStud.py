from typing import Any
from datetime import date
from enum import *


class Persona:
    _nome:str
    _cognome:str
    _data_nascita:date

    def __init__(self,nome:str,cognome:str,data_nascita:str):

        self._nome=nome
        self._cognome=cognome
        self._data_nascita=data_nascita

    def Name(self):
        return self._nome 
    
    def Cognome(self):
        return self._cognome
    
    def Data(self):
        return self._data_nascita
    
    # def __hash__(self)->int:
    #     return hash( (self.Name(),self.Cognome(),self.Data()) )
    
    # def __eq__(self,other:Any)->bool:
    #     if other is None or not isinstance(other,type(self)) or hash(self) != hash(other):
    #         return False
    #     else:
    #         return (self.Name(),self.Cognome(),self.Data()) == (other.Name(),other.Cognome(),other.Data())
        


class Genere(StrEnum):
    uomo=auto()
    donna=auto()

class Donna(Persona):
    _maternità:int
    _genere:str

    def __init__(self,genere:str,maternità:int):
        try:
            if genere != Genere.donna:
                raise f"Errore! Non hai inserito una donna"
        finally:
            self._genere=genere

        try:
            if maternità < 0 or maternità == float:
                raise "Errore inserisci 0 o maggiore" 
        finally:
            self._maternità=maternità

    def Genere(self):
        return self._genere
        
    def Maternità(self):
        return self._maternità


    # def __hash__(self)->int:
    #     return hash( (self.Name(),self.Cognome(),self.Data()) )
    
    # def __eq__(self,other:Any)->bool:
    #     if other is None or not isinstance(other,type(self)) or hash(self) != hash(other):
    #         return False
    #     else:
    #         return (self.Name(),self.Cognome(),self.Data()) == (other.Name(),other.Cognome(),other.Data())

class Uomo(Persona):
    _genere:str
    def __init__(self,genere:str):
        try:
            if genere != Genere.uomo:
                raise f"Errore! Non hai inserito un uomo"
        finally:
            self._genere=genere

    def PosizioneMilitare(self,pos_mil=None):
        if pos_mil:
            self.pos_mil=pos_mil

    def __str__(self):
        if self.pos_mil:
            return f"{self._nome}"
        
    
