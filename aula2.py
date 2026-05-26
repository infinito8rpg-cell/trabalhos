# Exercício 1 – Tupla com dias úteis da semana

dias_uteis = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta")

print(dias_uteis[0])    # Segunda  <- primeiro (índice 0)
print(dias_uteis[-1])   # Sexta    <- último (índice -1)
print(len(dias_uteis))  # 5

# Exercício 2 – Notas maiores ou iguais a 5

notas = (8, 3, 7, 5, 2, 9, 4)

for nota in notas:
    if nota >= 5:
        print(nota)  # 8, 7, 5, 9

# Exercício 3 – count e index

numeros = (4, 7, 2, 9, 1, 5)

quantidade = numeros.count(7)
print(quantidade)        # 1  <- o 7 aparece 1 vez

posicao = numeros.index(9)
print(posicao)           # 3  <- o 9 está no índice 3

# Exercício 4 (Desafio) – Classificação de temperaturas

temperaturas = (36.5, 37.2, 38.0, 36.8, 39.1)

for temp in temperaturas:
    if temp < 37.5:
        print(f"{temp}°C → Normal")
    elif temp <= 38.5:
        print(f"{temp}°C → Febre moderada")
    else:
        print(f"{temp}°C → Febre alta")