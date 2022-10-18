nome = input()
idade = int(input())
salario  = float(input())
sexo = input()
civil = input()

certo = 0

if len(nome) > 3:
    print("ok")
    certo += 1
else:
    print("nada ok")   

if idade > 0 and idade <= 150:
    print("ok")
    certo += 1
else:
    print("nada ok")  

if salario > 0:
    print("ok")
    certo += 1
else:
    print("nada ok")

if sexo == 'f' or sexo == 'm':
    print("ok")
    certo += 1
else:
    print("nada ok")

if civil == 's' or civil == 'c' or civil == 'v' or civil == 'd':
    print("ok")
    certo += 1
else:
    print("nada ok")    


if certo == 5:
    print("sim")
else:
    print("nao")    