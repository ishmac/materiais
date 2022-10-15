n1 = int(input())
n2 = int(input())
n3 = int(input())


if n1 >= 1000 and n2 >= 1000:
    print("SIM")
elif n1 >= 1000 and n3 >= 1000:
    print("SIM")
elif n2 >= 1000 and n3 >= 1000:
    print("SIM") 
else:
    print("NAO")          