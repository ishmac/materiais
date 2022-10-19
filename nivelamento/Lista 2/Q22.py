def potencia(b,n):
	if n == 0:
		return 1 
	else:
		return b * potencia(b, n-1)

b = int(input())
n = int(input())

res = potencia(b,n)
print(res)