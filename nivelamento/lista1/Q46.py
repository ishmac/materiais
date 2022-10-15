peso = float(input())
distancia = float(input())

valorPeso = peso * 25
valorDistancia = distancia * 0.10
iC = 12 / 100 * (valorPeso + valorDistancia)

imposto = valorPeso + valorDistancia + iC

print(imposto) 
