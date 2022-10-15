d1 = int(input())
d2 = int(input())
rodadas = int(input())

if d1 < 1 or d1 > 6:
	print("Entrada invalida")
elif d2 < 1 or d2 > 6:
	print("Entrada invalida")
elif rodadas < 0:
	print("Entrada invalida")
else:
	if (d1 + d2) == 12:
		pontosVida = d1 + d2 + 1
		tipo = "CONSTRICAO"
		print(tipo)
		print(pontosVida)
	elif d1 + d2 < 5:
		tipo = "POLEN"
		pontosVida = (d1 + d2 + 1) * rodadas
		print(tipo)
		print(pontosVida)
	else:
		tipo = "FRAQUEZA"
		pontosVida = d1*d2
		print(tipo)
		print(pontosVida)



		