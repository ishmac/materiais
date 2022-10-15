# 0 pedra
# 1 papel 
# 2 tesoura

user = int(input())
pc = int(input())

if user == 0 and pc == 0:
    print("empate")
elif user == 0 and pc == 1:    
    print("computador venceu")
elif user == 0 and pc == 2:
    print("usuario venceu")   
elif user == 1 and pc == 0:
    print("usuario venceu") 
elif user == 1 and pc == 1:
    print("empate") 
elif user == 1 and pc == 2:
    print("computador venceu")       
elif user == 2 and pc == 0:
    print("computador venceu")
elif user == 2 and pc == 1: 
    print("usuario venceu")   
elif user == 2 and pc == 2:
    print("empate")    