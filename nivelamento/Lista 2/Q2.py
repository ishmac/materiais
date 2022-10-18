#lista = [] 

n =int(input())
cont = 10
rodando = True
soma = 0
somaInv = 0

if n < 10:
    print(n)
elif n > 10:
    n1 = n % 10
    soma += n1

    while rodando:
    
        numero = n // cont % 10
        soma += numero
        cont = cont * 10
        if n / cont < 1:
            rodando = False

    
    while soma > 0:
        resto = soma % 10 
        somaInv = somaInv * 10 + resto
        soma = soma // 10 

    print(somaInv)    
