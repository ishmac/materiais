tempo = int(input())
hora = 0 
minutos = tempo / 60 

if minutos > 60:
    hora += 1 
    minutos -= 60

segundos = minutos - int(minutos)
segundos = segundos * 60

print("{}h {}m {}s".format(hora,int(minutos),int(segundos)))