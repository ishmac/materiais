n = int(input())
lista = []

for prim in range(2,n):
    if (n % prim == 0):
        lista.append(prim)

if (lista == []) :
    print("PRIMO")       
else:
    print(lista)
