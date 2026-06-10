soma = 0
while soma <= 100:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    if num < 0:
        continue
    soma += num
print(f"Soma final: {soma}")


