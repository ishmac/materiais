gramas = float(input())
qtdBebidas = int(input())
qtdSobremesa = int(input())

kiloUser = gramas / 1000

total = (kiloUser * 26.9) + (qtdBebidas * 3.5) + (qtdSobremesa * 3)
print(round(total,2))