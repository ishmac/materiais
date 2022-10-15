qtdVendidos = int(input())

arrecadado = qtdVendidos * 12 
lucroEspetos = arrecadado * 0.83

empregado = 100 + (lucroEspetos * 0.20)

lucroLiquido = lucroEspetos - empregado
print(round(lucroLiquido,2))