import datetime

nome1 = input("Digite o nome da primeira pessoa: ")
data_texto1 = input("Digite a data de nascimento (ex: 25/12/2008): ")

partes1 = data_texto1.split("/")
dia1 = int(partes1[0])
mes1 = int(partes1[1])
ano1 = int(partes1[2])

data1 = datetime.datetime(ano1, mes1, dia1)

nome2 = input("Digite o nome da segunda pessoa: ")
data_texto2 = input("Digite a data de nascimento (ex: 15/05/2010): ")

partes2 = data_texto2.split("/")
dia2 = int(partes2[0])
mes2 = int(partes2[1])
ano2 = int(partes2[2])

data2 = datetime.datetime(ano2, mes2, dia2)

if data1 < data2:
    print(f"A pessoa mais velha é: {nome1}")
elif data2 < data1:
    print(f"A pessoa mais velha é: {nome2}")
else:
    print("As duas pessoas têm a mesma idade!")
