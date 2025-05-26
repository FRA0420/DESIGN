import re

class PartitaIVA(str):
    def __new__(cls,p_iva:str):
        if not re.fullmatch(r'^[0-9]{11}$',p_iva):
            raise ValueError("Partita IVA inserita non corretta")
        
        return super().__new__(cls,p_iva)