from telefono import *
from enum import *


class Studente:

    _mat: int #<<imm>> noto alla nascita
    _genere: str
    _telefono: set[Telefono] #noto alla nascita
    _email: set[Email] #certamente non noto alla nascita


class Telefono(str):
    def __new__(cls,tel:str):
        if re.fullmatch(r'^d{10}',tel):
            return super().__new__(cls,tel)
        raise ValueError(f"{tel} non è un  numero di telefono italiano valido")
    



