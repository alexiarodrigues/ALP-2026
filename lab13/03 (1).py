for i in range(5):
    print(i)
    
#i: 0,1,2,3,4
#repetições: 5

for x in range (1,10,2):
    print(x)

#i; 1,3,5,7,9
#5x

for n in range(5,0,-1):
    print(n)
    
#i:5,4,3,2,1
#5x

soma = 0
for i in range(0, 10, 5):
    soma += i
    print(i)
    print(soma)
#i:0,0,5,5
#4x

soma = 0
for i in range(5, 10):
    print(i)
    print(soma)
    if i % 2 == 0:
        soma += i
#i:0,6,0,7,6,8,6,9,14
#9x

n = 100
for i in range(100, 50, -10):
    sub = n - i
    print(i)
    print(sub)
#i:100,0,90,10,80,20,70,30,60,40
#10x

soma = 0
for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    soma += i
    print(i, soma)
#i:0,0,1,2,3,4,7,5,12,6,18
#11x