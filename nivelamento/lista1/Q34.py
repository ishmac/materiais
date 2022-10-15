mols = int(input())
volume = float(input())
temp = float(input())

tempKelvin = temp + 273.1
r = 0.082057 

pressao = (mols * r  * tempKelvin) / volume
print(pressao)