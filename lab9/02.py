#a
n = int(input("Digite um número: "))
if n % 2 == 0:
    if n > 10:
        print("A")
    elif n == 10:
        print("B")
    else:
        print("C")
elif n > 5:
    print("D")
else:
    print("E")
#b
soma = 0
produto = 3
valor = int(input("Digite um valor: "))
cont = 1
while(cont <= valor):
    if soma > produto:
        break
    soma += cont
    if cont % 2 != 0:
        produto *= cont
    cont += 1
print(soma, produto)

