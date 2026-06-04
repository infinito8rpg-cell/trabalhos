# Exercício 1 – Animal (mãe) e Cachorro (filha)

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo")


class Cachorro(Animal):
    def latir(self):
        print(f"{self.nome} está latindo: Au au!")


# Testando
dog = Cachorro("Rex")
dog.comer()   # herdado de Animal  → Rex está comendo
dog.latir()   # próprio do Cachorro → Rex está latindo: Au au!
