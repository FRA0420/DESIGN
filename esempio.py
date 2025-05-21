#voglio rappresentare il genere uomo,donna
class Genere:
    def __init__(self,is_woman:bool):
        self.is_woman=is_woman
    def __str__(self):
        if self.is_woman:
            return "donna"
        else:
            return "uomo"
class Studente:
    def __init__(self,nome:str,genere:Genere):
        self.nome = nome
        self.genere = genere
    def __str__(self):
        return f"nome='{self.nome}', di genere {self.genere}"
    
if __name__ == '__main__':
    donna = Genere(True)
    uomo = Genere(False)

alice = Studente("alice",donna)
biagio = Studente("Biagio",uomo)

print('alice',alice)
print('biagio',biagio)

