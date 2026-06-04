# Exercício 3 – Funcionario (mãe) e Gerente (filha)

class Funcionario:
    def __init__(self, nome, salario):
        self.nome    = nome
        self.salario = salario

    def exibir(self):
        print(f"Nome: {self.nome} | Salário: R$ {self.salario:.2f}")


class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def salario_total(self):
        return self.salario + self.bonus


# Testando
g = Gerente("Fernanda", 5000.0, 1500.0)
g.exibir()                              # herdado de Funcionario
print(f"Salário total: R$ {g.salario_total():.2f}")  # 6500.00
