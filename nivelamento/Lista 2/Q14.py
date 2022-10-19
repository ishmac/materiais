listaRes = eval(input())
soma = 0
mult = 1

for i in range(len(listaRes)):
    soma += listaRes[i]
    mult *= listaRes[i]

res = (soma,mult)
print(res)	
