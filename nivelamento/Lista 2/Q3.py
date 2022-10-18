
num = int(input())
fat = 1
cont = 1 

if num == 0:
    fat = 1

while cont < (num + 1):
    fat = fat * cont 
    cont += 1 

print(fat)       