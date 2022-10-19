nParc = int(input())
parcIni = float(input())
soma = 0
c = 0
while c < nParc:
     
    parcIni *= 1.30
    soma += parcIni
    c += 1
print(round(soma,2))
