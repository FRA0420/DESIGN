from typing import Any
class IntGZ(int): #greter than zero
    def __new__(cls, v:Any | int | float | str | bool):

        value:int = super().__new__(cls,v)

        if value <= 0:
            raise ValueError("Valore deve essere maggiore di zero")
        return value
        