nomeCabeca = input()
d1 = int(input())
d2 = int(input())

if d1 > 10 or d1 < 1:
	print("Entrada invalida")
elif d2 > 10 or d2 < 1:
	print("Entrada invalida")
else:
	if nomeCabeca == "AAMEUL":
		pVida = 8 + (d1 + d2)
		print(pVida)
	elif nomeCabeca == "HETHRADIAH":
		pVida = (d1+d2)*2
		print(pVida)
	elif nomeCabeca == "RAKSHASA":
		pVida = 10 + (d1+d2)
		print(pVida)
	else:
		print("Entrada invalida")

		
	