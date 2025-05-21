from datetime import date

class Ordine:
    _data_stipula:date
    _descrizione:str
    _imponibile:float

    def __init__(self,data_stipula:date,descrizione:str,imponibile:float):
        self.setData(data_stipula)
        self.setDescrizione(descrizione)
        self.imponibile(imponibile)


    def setData(self,data_stipula:date):
        self._data_stipula=data_stipula
    
    def setDescrizione(self,descrizione:str):
        self._descrizione=descrizione

    def setImponibile(self,imponibile:float):
        self._imponibile=imponibile

    def data(self):
        return self._data_stipula
    def descrizione(self):
        return self._descrizione
    def imponibile(self):
        return self._imponibile
    