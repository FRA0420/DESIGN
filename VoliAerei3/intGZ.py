from typing import Self

class IntGZ(int): #greater than zero
    
    def __new__(cls, v: Self | int | float | str | bool):

        value:int = super().__new__(cls,v)

        if value <= 0:
            raise ValueError("Valore deve essere maggiore di zero")
        return value
        