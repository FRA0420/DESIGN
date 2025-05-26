# from typing import Self
from datetime import date

class DataGE1895(date):  #data maggiore del 1895
    def __new__(cls,year:int,
                month:int,
                day:int):
        if year < 1895:
            raise ValueError("La data non può essere maggiore")
        return super().__new__(cls,year=year,
                               month=month,
                               day=day)