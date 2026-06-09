vitorias = 0
empates = 0
derrotas = 0
pontos = 0

n = int(input())

for i in range(n):
    galo = int(input())
    adversario = int(input())

    if galo > adversario:
        vitorias += 1
        pontos += 3
    elif galo == adversario:
        empates += 1
        pontos += 1
    else:
        derrotas += 1

print("Vitórias:", vitorias)
print("Empates:", empates)
print("Derrotas:", derrotas)
print("Pontuação:", pontos)
