tipo = input()
valorDado = int(input())
turnos = int(input())

if valorDado < 1 or valorDado > 4:
	print("Entrada invalida")
else:
	if tipo == "CAUDA":
		dano = valorDado * turnos
		print(dano)
	elif tipo == "CUSPE":
		dano = (2*valorDado) * turnos
		print(dano)
	elif tipo == "PATADA":
		dano = (2*valorDado) - 5 
		print(dano)