qtdPO = int(input())
armadura = input()
fator = int(input())

if fator > 8 or fator < 1:
	print("Entrada invalida")

elif armadura == "INTEIRA":
	if qtdPO < 200:
		print("PO insuficiente")
	else:	
		rest = (30 * fator) - 20	
		print(rest)
elif armadura == "MALHA":
	if qtdPO < 50:
		print("PO insuficiente")
	else:	
		rest = (15 * fator) - 1	
		print(rest)
elif armadura == "PLACA":
	if qtdPO < 100:
		print("PO insuficiente")
	else:	
		rest = (20*fator)-18
		print(rest)
else: 
	print("Entrada invalida")