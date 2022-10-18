
nota = float(input())
rodando = True
while rodando:
    if nota >= 0 and nota <= 10:
        print("valor valido")
        rodando = False
    else:
        print("valor invalido")    
        nota = float(input())
