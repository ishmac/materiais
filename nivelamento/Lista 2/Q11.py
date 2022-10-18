num = int(input())
fat = 1
cont = 1 

if num == 0:
    fat = 1
    print(fat)	
elif num < 0:
    num = -1 
    print(num)
else:
    while cont < (num + 1):
        fat = fat * cont 
        cont += 1 

    print(fat)       