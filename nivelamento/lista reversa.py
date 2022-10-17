'''
Faça um programa que peça um número inteiro positivo e em seguida mostre uma lista com este número invertido.

Ex: 123456 -> [6,5,4,3,2,1].

 

OBS: NÃO UTILIZAR STRING EM MOMENTO ALGUM.
'''
num = int(input())
lista = []
while num >= 1:
    num2 = num % 10
    lista.append(num2)
    num = num // 10
print(lista)
