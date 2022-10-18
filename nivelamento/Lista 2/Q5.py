n = int(input())
lista = [] 
listaF = [] 
cont = 10
rodando = True
vezes = 0 

if n < 10:
    lista.append(n)
elif n > 10:
    n1 = n % 10
    lista.append(n1)
    vezes += 1

    while rodando:
        
        numero = n // cont % 10
        lista.append(numero)
        cont = cont * 10
        if n / cont < 1:
            rodando = False

        vezes += 1    
        

for i in range(int(vezes / 2)):
    n = lista[i]
    lista[i] = lista[vezes - i - 1]
    lista[vezes - i - 1] = n 
		
cc = 0

while cc < vezes:
    lista[cc] = lista[cc]**2
    listaF.append(lista[cc])
    cc += 1 
print(listaF)    
