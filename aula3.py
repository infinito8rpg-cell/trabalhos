# Exercício 1 – Classe Produto com atributos nome e preco

class Produto:
    def __init__(self, nome, preco):
        self.nome  = nome   # atributo nome
        self.preco = preco  # atributo preco


# Criando dois objetos
p1 = Produto("Teclado", 150.00)
p2 = Produto("Mouse",    89.90)

# Imprimindo os atributos
print(p1.nome, p1.preco)   # Teclado 150.0
print(p2.nome, p2.preco)   # Mouse 89.9

# Exercício 2 – Produto com método desconto()

class Produto:
    def __init__(self, nome, preco):
        self.nome  = nome
        self.preco = preco

    def desconto(self, percentual):
        # Calcula o valor a descontar e retorna o novo preço
        valor_desconto = self.preco * (percentual / 100)
        return self.preco - valor_desconto


# Testando
p1 = Produto("Teclado", 100.0)
p2 = Produto("Mouse",    80.0)

print(p1.desconto(10))   # 90.0  <- 10% de desconto
print(p2.desconto(25))   # 60.0  <- 25% de desconto

# Exercício 3 – Classe Carro com acelerar() e frear()

class Carro:
    def __init__(self, marca, modelo):
        self.marca     = marca
        self.modelo    = modelo
        self.velocidade = 0       # começa sempre em 0

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade -= 10
        if self.velocidade < 0:   # não deixa passar de 0
            self.velocidade = 0


# Criando o objeto
carro = Carro("Toyota", "Corolla")

# Acelerando 3 vezes (+30) e freando 1 vez (-10) → velocidade final: 20
carro.acelerar()
carro.acelerar()
carro.acelerar()
carro.frear()

print(carro.velocidade)   # 20

# Exercício 4 (Desafio) – Classe ContaBancaria

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo   = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor

    def extrato(self):
        print(f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")


# Testando todos os métodos
conta = ContaBancaria("Ana", 500.0)

conta.extrato()          # Titular: Ana | Saldo: R$ 500.00

conta.depositar(200.0)
conta.extrato()          # Titular: Ana | Saldo: R$ 700.00

conta.sacar(150.0)
conta.extrato()          # Titular: Ana | Saldo: R$ 550.00

conta.sacar(1000.0)      # Saldo insuficiente
conta.extrato()          # Titular: Ana | Saldo: R$ 550.00 (não mudou)