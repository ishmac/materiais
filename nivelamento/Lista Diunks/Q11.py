lista = []
impar = 0
par = 0 

for i in range(10):
    num = int(input())
    lista.append(num)

for c in lista:
    if c % 2 == 0:
        par += 1
    else:
        impar += 1

print(par)
print(impar)