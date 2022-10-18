n = int(input())
lista = [] 
cont = 10
rodando = True
if n < 10:
    lista.append(n)
elif n > 10:
    n1 = n % 10
    lista.append(n1)

    while rodando:
  
        numero = n // cont % 10
        lista.append(numero)
        cont = cont * 10
        if n / cont < 1:
            rodando = False
        
    print(lista)    
