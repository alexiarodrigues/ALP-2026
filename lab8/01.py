cont = 5
while cont > 0:
    num = int(input("Digite um número inteiro: "))
    cont -= 1
    if num % 2 == 0:
        continue
     #se o número for par o continue pula para o print
     #e repete dnv
    print(f'{num} é um número ímpar')

