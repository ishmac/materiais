cat = float(input("Cateto : "))
catOp = float(input("Cateto oposto: "))
hip = float(input("Hipotenusa: "))


if (cat**2) + (catOp**2) == (hip**2):
    print("Correto")
else:
    print("Tente novamente, mas lembre-se: ")
    print("Em um triângulo retângulo a soma dos quadrados dos catetos é igual ao quadrado da hipotenusa.")
    print("\nCom organização e tempo, acha-se o\nsegredo de fazer tudo e bem feito.\n\t\t\t\t\t\t'Pitágoras'")