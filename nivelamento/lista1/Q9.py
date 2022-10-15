produto = float(input())
novoPreco = 0 

if produto <= 100:
    produto = produto * 1.05
    print("{} ryous".format(round(produto,2)))
    print("Aumento de 5 porcento")

elif produto > 100:
    produto = produto * 1.15    
    print("{} ryous".format(round(produto,2)))
    print("Aumento de 15 porcento")