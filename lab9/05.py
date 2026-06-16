soma = 0
cont = 0
quant = int(input("Digite a quantidade de números que deseja digitar: "))
N = quant
while N > 0:
    numero = int(input("Digite um número: "))
    soma += numero
    cont += 1
    N -= 1
media = soma/cont
print("A soma dos números digitados é: ", soma)
print("A quantidade de números digitados é: ", cont)
print("A média é: ", media)
