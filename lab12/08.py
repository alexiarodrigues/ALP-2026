import datetime

hoje = datetime.datetime.now()
ano_atual = hoje.year

print("--- Dados da Primeira Pessoa ---")
nome1 = input("Nome: ")
data_texto1 = input("Data de nascimento (dd/mm/aaaa): ")
partes1 = data_texto1.split("/")
dia1 = int(partes1[0])
mes1 = int(partes1[1])

niver1 = datetime.datetime(ano_atual, mes1, dia1)


print("\n--- Dados da Segunda Pessoa ---")
nome2 = input("Nome: ")
data_texto2 = input("Data de nascimento (dd/mm/aaaa): ")
partes2 = data_texto2.split("/")
dia2 = int(partes2[0])
mes2 = int(partes2[1])

niver2 = datetime.datetime(ano_atual, mes2, dia2)

dias_pessoa1 = abs((niver1 - hoje).days)
dias_pessoa2 = abs((niver2 - hoje).days)

print("\n--- Resultado ---")
if dias_pessoa1 < dias_pessoa2:
    print(f"O aniversário mais próximo é o de {nome1}!")
else:
    print(f"O aniversário mais próximo é o de {nome2}!")
