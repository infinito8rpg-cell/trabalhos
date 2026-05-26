# ============================================================
#   EXERCÍCIOS — LISTAS EM PYTHON
#   Prof. Diego | CEEP Pedro Boaretto Neto
# ============================================================


# ------------------------------------------------------------
# Exercício 1
# Criar uma lista com 5 nomes e imprimir o primeiro e o último.
# ------------------------------------------------------------
print("=== Exercício 1 ===")

colegas = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

print(colegas[0])   # Ana      <- primeiro (índice 0)
print(colegas[-1])  # Eduardo  <- último (índice -1)


# ------------------------------------------------------------
# Exercício 2
# Partir de [7, 4, 9, 6, 3], adicionar 8, remover 4,
# imprimir a lista final e seu tamanho.
# ------------------------------------------------------------
print("\n=== Exercício 2 ===")

numeros = [7, 4, 9, 6, 3]

numeros.append(8)   # [7, 4, 9, 6, 3, 8]
numeros.remove(4)   # [7, 9, 6, 3, 8]

print(numeros)      # [7, 9, 6, 3, 8]
print(len(numeros)) # 5


# ------------------------------------------------------------
# Exercício 3
# Percorrer [8, 3, 7, 5, 2, 9, 4] e imprimir só as notas < 5.
# ------------------------------------------------------------
print("\n=== Exercício 3 ===")

notas = [8, 3, 7, 5, 2, 9, 4]

for nota in notas:
    if nota < 5:
        print(nota)  # 3, 2, 4


# ------------------------------------------------------------
# Exercício 4 — Desafio
# Criar lista vazia, percorrer 1..20 e guardar só os pares.
# ------------------------------------------------------------
print("\n=== Exercício 4 (Desafio) ===")

pares = []

for numero in range(1, 21):
    if numero % 2 == 0:   # verifica se é par
        pares.append(numero)

print(pares)        # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(len(pares))   # 10