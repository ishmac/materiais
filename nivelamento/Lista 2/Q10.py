frase = input()
lista = [] 
tot = 0
for i in frase:
    if 'a' < i < 'e' or 'e' < i < 'i' or 'i' < i < 'o' or 'o' < i < 'u' or 'u' < i <= 'z' and i != '_':
        tot += 1
        lista.append(i)
    if 'A' < i < 'E' or 'E' < i < 'I' or 'I' < i < 'O' or 'O' < i < 'U' or 'U' < i <= 'Z' and i != '_':
        tot += 1
        lista.append(i)    

print(tot)
print(*lista, sep = "")
