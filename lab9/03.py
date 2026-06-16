#a
i = 0
while i < 10:
    print(i)
    i += 1
#b
x = 2
while x <= 32:
    print(x)
    x = x * 2
#c
n = 100
cont = 0
while n > 1:
    print(n, cont)
    n = n // 2
    cont += 1
#d
a = 1
while True:
    print(a)
    a = a + 3
    if a > 10:
        break
#e
soma = 0
i = 0
while i < 10:
    print(i, soma)
    i += 1
    if i == 5:
        break
    soma += i
#f
soma = 0
i = 0
while i < 10:
    print(i, soma)
    i += 1
    if i % 2 == 0:
        continue
    soma += i
#g
soma = 0
i = 0
while i < 10:
    print(i, soma)
    i += 1
    if i == 3:
        continue
    if i == 7:
        break
    soma += i

