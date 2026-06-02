conta_total = 0
while True:
    print("Cardápio Cantina")
    print("1. Açaí 300ml - R$ 12")
    print("2. Mousse - R$ 6,50")
    print("3. Salada de frutas - R$ 10")
    print("4. Fechar a conta")
    num = int(input("Digite o número da opção desejada:"))
    if num == 1:
        conta_total += 12
    if num == 2:
        conta_total += 6,50
    if num == 3:
        conta_total += 10
    if num == 4:
        print(f"Conta fechada. O total a pagar é: R$ {conta_total}")
        break
    