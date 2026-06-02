
conta_total = 0
while True:
    print("\n--- Cardápio Cantina ---")
    print("1. Açaí 300ml - R$ 12")
    print("2. Mousse - R$ 6,50")
    print("3. Salada de frutas - R$ 10")
    print("4. Fechar a conta")
    opcao = int(input("Digite o número da opção desejada: "))
 
    if opcao == 1:
        conta_total += 12
        
    if opcao == 2:
        conta_total += 6.50

    if opcao == 3:
        conta_total += 10

    if opcao == 4:
        print("Conta fechada! O total a pagar é: R$ {conta_total:.2f}")
        break
    