#B)
def ola(nome,genero):
    oi= input("Gênero?")
    if oi == "feminino":
        return f"Olá {nome} boas vinda!"
    elif oi =="masculino":
            return f"Olá {nome} boas vinda!"
    else:
        return f"Olá {nome} boas vindas!"

print(ola("Mila","feminino"))
print(ola("Leo", "neutro"))
print(ola("Alan", "masculino"))
