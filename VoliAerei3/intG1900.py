from typing import Self

class intG1900(int):
    #Tipo di dato specializzato Intero > 1900
    def __new__(cls, v: Self | int | str | bool | float):
        value: int = super().__new__(cls,v)
        
        if value <= 1900:
            raise ValueError(f"The value {v} must be greater than 1900")
        
        else:
            return value