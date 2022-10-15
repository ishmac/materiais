tipo = input()
qtd = int(input())

if qtd < 0:
    print("Entrada invalida")
else: 
    if tipo == "TERRESTRE":
        dragao = "DROGON"
        baf = qtd / 150

        if baf <= 1:
            baf = 1
            print(dragao)
            print(baf) 
        elif qtd % baf != 0:
            baf = int(baf) + 1
            print(dragao)
            print(baf)  
        else:
            print(dragao)
            print(int(baf))


    elif tipo == "AEREO":
        dragao = "RHAEGAL"
        baf = qtd / 30 

        if baf <= 1:
            baf = 1
            print(dragao)
            print(baf) 
        elif qtd % baf != 0:
            baf = int(baf) + 1
            print(dragao)
            print(baf)  
        else:
            print(dragao)
            print(int(baf))

    elif tipo == "MARITIMO":
        dragao = "VISERION"
        baf = qtd / 40

        if baf <= 1:
            baf = 1
            print(dragao)
            print(baf) 
        elif qtd % baf != 0:
            baf = int(baf) + 1
            print(dragao)
            print(baf)  
        else:
            print(dragao)
            print(int(baf))
            
    else: 
        print("Entrada invalida")    

