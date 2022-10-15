nome = str(input())
nota = float(input())
frequencia = int(input())
if nota >= 5 and frequencia >=45 : 
	print("{} - Aprovado".format (nome))
elif nota < 5 and frequencia >=45 : 
	print("{} - Reprovado".format (nome))
elif nota >=5 and frequencia <45 : 
	print("{} - Reprovado".format (nome))
elif nota <5 and frequencia <45 : 
	print("{} - Reprovado".format (nome) )