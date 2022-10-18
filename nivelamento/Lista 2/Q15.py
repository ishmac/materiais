res = input()
tot = 0

for i in res:
    if 'A' < i < 'E' or 'E' < i < 'I' or 'I' < i < 'O' or 'O' < i < 'U' or 'U' < i <= 'Z' and i != '_':
        tot += 4.17
    else:
        tot += 3.15    

print(round(tot,2))