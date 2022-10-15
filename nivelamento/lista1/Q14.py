cod = int(input())
salario = float(input())

if cod == 101:
    salario = salario * 1.10
    print(round(salario,2))
    print("Aumento de 10 por cento")
elif cod == 102:
    salario = salario * 1.30
    print(round(salario,2))
    print("Aumento de 30 por cento")    