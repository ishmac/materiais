idade = int(input("Idade: "))
jaVacinado = str(input("Ja vacinado: "))

if idade > 60:
	print("False")
elif idade >= 40 and idade < 60:
	print("True")
else:
	print("False")