distKM = float(input())
cha = float(input())

distM = distKM * 100

necessario = 30 * distM 

print(necessario)

if cha < necessario:
    print("nao vai conseguir")
elif cha >= necessario:
    print("vai conseguir")    