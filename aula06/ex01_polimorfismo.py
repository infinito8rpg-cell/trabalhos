# Exercício 1 – Funcionario (mãe), Vendedor e Gerente (filhas)

class Funcionario:
    def calcular_salario(self):
        return 0


class Vendedor(Funcionario):
    def __init__(self, salario_fixo, comissao):
        self.salario_fixo = salario_fixo
        self.comissao     = comissao

    def calcular_salario(self):
        return self.salario_fixo + self.comissao


class Gerente(Funcionario):
    def __init__(self, salario_fixo, bonus):
        self.salario_fixo = salario_fixo
        self.bonus        = bonus

    def calcular_salario(self):
        return self.salario_fixo + self.bonus


v = Vendedor(2000, 500)
g = Gerente(5000, 1500)

print(v.calcular_salario())   # 2500
print(g.calcular_salario())   # 6500
