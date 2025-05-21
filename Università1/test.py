from typing import Any
import re
from matricola import Matricola
# from email import *
from cf import CodiceFiscale
from ind import Indirizzo

if __name__ == "__main__":
    cf1 = CodiceFiscale("RSSMRA80A01H501U")
    cf2 = CodiceFiscale("rssmra80a01h501u")  # deve essere uguale a cf1

    indirizzo1 = Indirizzo("Via Roma", "10")
    indirizzo2 = Indirizzo("Via Roma", "10")  # uguale

    print(cf1 == cf2)  # ✅ True
    print(indirizzo1 == indirizzo2)  # ✅ True

    insieme = {cf1, cf2, indirizzo1, indirizzo2}
    print(f"Oggetti unici nel set: {len(insieme)}")  # ✅ Deve stampare 2