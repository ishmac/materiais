x = int(input())
taxaFixa = 50

if x < 100:
    total = taxaFixa + x*0.5
elif x >= 100 and x < 250:
    total = taxaFixa + x*0.75
elif x >= 250 and x < 500:
    total = taxaFixa + x*1
elif x >= 500:
    total = taxaFixa + x*1.25   

print(round(total,2))