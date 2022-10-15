x = int(input())
taxaFixa = 20

if x < 10:
    total = taxaFixa + x*2
elif x == 10 and x < 20:
    total = taxaFixa + x*2.5
elif x >= 20 and x < 40:
    total = taxaFixa + x*2.75
elif x >= 40:
    total = taxaFixa + x*3    

print(round(total,2))
