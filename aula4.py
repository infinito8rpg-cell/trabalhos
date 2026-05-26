# Exercício 1 – Classe Produto com encapsulamento

class Produto:
    def __init__(self, nome, preco):
        self.__nome  = nome
        self.__preco = preco

    # --- Getters ---
    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    # --- Setters com validação ---
    def set_nome(self, nome):
        if len(nome) > 0:
            self.__nome = nome
        else:
            print("Erro: nome não pode ser vazio")

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Erro: preço não pode ser negativo")


# Testando
p = Produto("Teclado", 150.0)

print(p.get_nome())    # Teclado
print(p.get_preco())   # 150.0

p.set_preco(200.0)
print(p.get_preco())   # 200.0

p.set_preco(-10)       # Erro: preço não pode ser negativo
p.set_nome("")         # Erro: nome não pode ser vazio
print(p.get_nome())    # Teclado  <- não mudou

# Exercício 2 – Classe Pessoa com encapsulamento

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome  = nome
        self.__idade = idade

    # --- Getters ---
    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    # --- Setters com validação ---
    def set_nome(self, nome):
        if len(nome) > 0:
            self.__nome = nome
        else:
            print("Erro: nome não pode ser vazio")

    def set_idade(self, idade):
        if 0 <= idade <= 120:
            self.__idade = idade
        else:
            print("Erro: idade deve estar entre 0 e 120")

    # --- Método de exibição ---
    def apresentar(self):
        print(f"Nome: {self.__nome} | Idade: {self.__idade} anos")


# Testando
p = Pessoa("Carlos", 17)
p.apresentar()           # Nome: Carlos | Idade: 17 anos

p.set_idade(18)
p.apresentar()           # Nome: Carlos | Idade: 18 anos

p.set_idade(200)         # Erro: idade deve estar entre 0 e 120
p.set_nome("")           # Erro: nome não pode ser vazio
p.apresentar()           # Nome: Carlos | Idade: 18 anos  <- não mudou

# Exercício 3 – ContaBancaria com encapsulamento

class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo   = 0          # saldo começa em 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Erro: o valor do depósito deve ser positivo")

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente")
        else:
            self.__saldo -= valor

    def get_saldo(self):
        return self.__saldo

    def extrato(self):
        print(f"Titular: {self.__titular} | Saldo: R$ {self.__saldo:.2f}")


# Testando
conta = ContaBancaria("Bruno")
conta.extrato()           # Titular: Bruno | Saldo: R$ 0.00

conta.depositar(500)
conta.extrato()           # Titular: Bruno | Saldo: R$ 500.00

conta.sacar(200)
conta.extrato()           # Titular: Bruno | Saldo: R$ 300.00

conta.depositar(-100)     # Erro: o valor do depósito deve ser positivo
conta.sacar(1000)         # Saldo insuficiente

print(conta.get_saldo())  # 300.0

# Exercício 4 (Desafio) – Classe Sensor com encapsulamento

class Sensor:
    def __init__(self, temperatura):
        self.__temperatura = None       # inicia vazio
        self.set_temperatura(temperatura)  # já valida na criação

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, valor):
        if -50 <= valor <= 150:
            self.__temperatura = valor
        else:
            print(f"Erro: {valor}°C fora do limite do sensor (-50 a 150)")

    def status(self):
        t = self.__temperatura
        if t is None:
            return "Sem leitura"
        elif t <= 80:
            return "Normal"
        elif t <= 120:
            return "Alerta"
        else:
            return "Critico"

    def exibir(self):
        print(f"{self.__temperatura}°C → {self.status()}")


# Testando com 4 temperaturas diferentes
s = Sensor(25)
s.exibir()                  # 25°C → Normal

s.set_temperatura(95)
s.exibir()                  # 95°C → Alerta

s.set_temperatura(135)
s.exibir()                  # 135°C → Critico

s.set_temperatura(-30)
s.exibir()                  # -30°C → Normal

s.set_temperatura(200)      # Erro: 200°C fora do limite do sensor