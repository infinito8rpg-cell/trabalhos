# Exercício 2 – Instrumento (mãe), Violao, Bateria e Piano (filhas)

class Instrumento:
    def tocar(self):
        print("Som genérico")


class Violao(Instrumento):
    def tocar(self):
        print("Violão: Plin plin!")


class Bateria(Instrumento):
    def tocar(self):
        print("Bateria: Tum tcha!")


class Piano(Instrumento):
    def tocar(self):
        print("Piano: Dó ré mi!")


instrumentos = [Violao(), Bateria(), Piano()]

for inst in instrumentos:
    inst.tocar()
