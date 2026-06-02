N = int(input("Quantos nÃºmeros quer digitar?"))
contador = 1
impares = 0
while contador == N:
    num = int(input("Digite um nÃºmero: "))
    if num % 2 != 0:
        impares += 1
        contador =+ 1
        #sem isso adicionado,o contador nunca aumenta
print(f"Quantidade de impares: {impares}")

#Codigo b
soma =  0
contador = 1
#sem o contador,n acontece as 10x repetidas
while soma <= 10:
    num = int(input("Digite um numero para somar: "))
    soma += num
    contador +=1 #como adicionamos a variavel,tb temos q adionar os valores dps do while
    
#c)Imprimir o maior nÃºmero digitado pelo usuÃ¡rio

maior = float('-inf') #caso contrario o "num>maior" nunca vai rodar
contador = 1
while contador <= 10: #a variavel n havia sido definida
    num = int(input("Digite um nÃºmero: "))
    if num > maior:
       maior = num
       contador += 1
print('O maior numero digitado é', maior)
