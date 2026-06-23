
import random
import time
N = random.randint(2, 10)
time.sleep(N)

print("AGORA!")
tempo_inicio = time.time()

input()
tempo_fim = time.time()
tempo_decorrido = tempo_fim - tempo_inicio
print(f"Se passaram {tempo_decorrido:.2f} segundos.")