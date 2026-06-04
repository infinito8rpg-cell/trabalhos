# Exercício 4 (Desafio) – Pagamento (mãe), Dinheiro, Cartao e Pix (filhas)

class Pagamento:
    def processar(self, valor):
        return valor


class Dinheiro(Pagamento):
    def processar(self, valor):
        return valor * 0.95          # 5% de desconto


class Cartao(Pagamento):
    def processar(self, valor):
        return valor * 1.02          # 2% de juros


class Pix(Pagamento):
    def processar(self, valor):
        return valor                 # sem alteração


pagamentos = [Dinheiro(), Cartao(), Pix()]
nomes      = ["Dinheiro", "Cartão ", "Pix    "]

for nome, pagamento in zip(nomes, pagamentos):
    resultado = pagamento.processar(100.0)
    print(f"{nome}: R$ {resultado:.2f}")
