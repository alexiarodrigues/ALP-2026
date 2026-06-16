#a
x1 = int(input("Digite um valor: "))
x2 = int(input("Digite outro valor: "))
if x1 == 0 or x2 == 0:
    print("Não é possível realizar a divisão!")
print(f"O resultado da divisão é: {x1 / x2}")

#b
cont = 0
soma = 0
x = int(input("Digite um valor: "))
while (cont < x):
    cont += 1
    soma += cont
print(f"A soma dos valores de 0 a {x} é {soma}")

#c
x = int(input("Digite o valor x: "))
y = int(input("Digite o valor y: "))
print(f"A soma de {x}+{y} é {x+y}")

#d
soma = 0
cont = 1
x = int(input("Digite um valor: "))
while cont <= x:
    if cont % 2 != 0:
        continue
    soma += cont
    cont += 1
print("A soma dos valores pare digitados é:", soma)
