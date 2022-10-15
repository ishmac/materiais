sal = float(input('Informe o salario atual: '))
#novo = sal + (sal * Reajuste)

if sal < 1212:
	novo = sal * 1.12
	print(round(novo,2))
elif sal >= 1212 and sal <= 5000:
	novo = sal * 1.08
	print(round(novo,2))
elif sal > 5000:
	novo = sal * 1.03
	print(round(novo,2))