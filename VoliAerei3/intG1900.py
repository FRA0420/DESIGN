from typing import Any

class intG1900(int):
    #Tipo di dato specializzato Intero > 1900
    def __new__(cls, v: Any):
        value: int = super().__new__(cls,v)
        
        if value <= 1900:
            raise ValueError(f"The value {v} must be greater than 1900")
        
        else:
            return value