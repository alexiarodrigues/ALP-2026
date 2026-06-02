import random
numero_secreto = (random.randint(1,10))
chances = 5
while chances > 0:
    palpite = int(input("Um valor:"))
    chances -= 1
    if palpite == numero_secreto:
        print("Parabens fia c acertou.")
        break
    else:
        if palpite < numero_secreto:
            print("Dica: Maior")
        else:
            print("Menor")