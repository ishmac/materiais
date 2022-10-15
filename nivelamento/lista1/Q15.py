qtd = int(input())

if qtd > 12:
    valor = qtd * 0.7
    print("O valor da sua compra eh: {}".format(round(valor,2)))
else:
    valor = qtd * 0.75
    print("O valor da sua compra eh: {}".format(round(valor,2)))    