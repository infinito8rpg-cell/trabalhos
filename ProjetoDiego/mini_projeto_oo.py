class Funcionario:
    def __init__(self, nome, matricula, salario_fixo):
        self.__nome = nome
        self.__matricula = matricula
        self.__salario_fixo = max(0, salario_fixo)  # não permite salário negativo

    # Getters
    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def get_salario_fixo(self):
        return self.__salario_fixo

    # Setter para salário fixo
    def set_salario_fixo(self, novo_salario):
        self.__salario_fixo = max(0, novo_salario)

    def calcular_salario(self):
        return self.__salario_fixo

    def exibir(self):
        print(f"Nome: {self.get_nome()} | Matricula: {self.get_matricula()} | "
              f"Tipo: {self.__class__.__name__} | Salario: R$ {self.calcular_salario():.2f}")


class CLT(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)

    def calcular_salario(self):
        return self.get_salario_fixo()


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_fixo, vendas=0):
        super().__init__(nome, matricula, salario_fixo)
        self.__vendas = max(0, vendas)

    def get_vendas(self):
        return self.__vendas

    def set_vendas(self, vendas):
        self.__vendas = max(0, vendas)

    def calcular_salario(self):
        comissao = self.__vendas * 0.10
        return self.get_salario_fixo() + comissao


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)
        self.__bonus = 1500.00

    def calcular_salario(self):
        return self.get_salario_fixo() + self.__bonus


# ==================== PROGRAMA PRINCIPAL ====================

if __name__ == "__main__":
    funcionarios = []

    f1 = CLT("Ana", "001", 3000.00)
    f2 = Vendedor("Bruno", "002", 2000.00, 12000.00)
    f3 = Gerente("Carla", "003", 5000.00)

    funcionarios.append(f1)
    funcionarios.append(f2)
    funcionarios.append(f3)

    print("=== FOLHA DE PAGAMENTO ===\n")
    for func in funcionarios:
        func.exibir()