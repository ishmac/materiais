#1

'''
def mostrarInfo(nome, idade):
	print("o nome é: {} e a idade é: {}".format(nome,idade))

nome = input()
idade = int(input())

mostrarInfo(nome,idade)
'''

#2

'''
def media(lista):
	soma = 0
	tamanho = 0

	for i in range(len(lista)):
		soma += lista[i] 
		tamanho += 1

	return soma / tamanho

lista = eval(input())
print(media(lista))
'''

#3
'''
def verifica(num):
	if num % 2 == 0:
		return True
	return False

num = int(input())
if verifica(num) == True:
	print("É par")
else:
	print("É impar")	
'''

#4
def somatorio(num: int) -> int:
	c = 0
	soma = 0
	while c <= num:
		soma += c 
		c += 1
	return soma 

num = int(input())
print(somatorio(num))

