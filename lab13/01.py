#a)
for i in range (1,5)
print (i * 2)
#corrigido:
for i in range(1,5):
    print (i*2)
#b)
soma = "0" # corrigindo o 0 é sem aspas
for num in range (10):
    soma = soma + num
print ("Soma:" , soma)

#c)
for num in range 3: #não há período/intervalo
print f"O dobro de (num) é:" #não há aspas
    print num*2 #não há aspas

#d)
numero = random.randint(1,10) #não há ":" erro de sintaxe
for i in range(3):
    n= input("Adivinhe o número:")
    if n == numero:
        print("Correto")
        break
