idade = int(input("Idade do atleta: "))

if idade < 5 and idade >= 1:
	print("Sem categoria")
elif idade >= 5 and idade <= 7:
	print("Infantil_A")
elif idade >= 8 and idade <= 10:
	print("Infantil_B")
elif idade >= 11 and idade <= 13:
	print("Infantil_C")
elif idade >= 14 and idade <= 17:
	print("Infantil_D")
elif idade >= 18:
	print("Senior")
else:
	print("Sem_categoria")
