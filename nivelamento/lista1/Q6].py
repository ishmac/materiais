n1 = int(input())

if  n1 % 3 == 0 and n1 % 5 == 0:
    print("PirlimPimpim") 
elif n1 % 5 == 0:
    print("Pimpim")
elif n1 % 3 == 0:
    print("Pirlim") 
else:
    print(n1)    