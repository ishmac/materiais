vezes = int(input())

lista = [1] 
n = 0 
varSoma = 0
cont = 0 

while cont < vezes-1:
    varSoma += 1
    n += varSoma
    
    cont += 1 
    lista.append(n+1)
    

print(lista)    
