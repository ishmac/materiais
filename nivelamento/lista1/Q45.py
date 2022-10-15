precoAbertura = float(input())
precoFechamento = float(input())

precoFinal = (precoFechamento * 100) / precoAbertura
variacao =  precoFinal - 100
print(variacao)	