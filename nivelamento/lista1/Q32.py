user = float(input())

rad = user * 57.29578
min = (rad - int(rad)) * 60
seg = (min - int(min)) * 60

radF = int(rad)
minF = int(min)
segF = int(seg)		 

print("{} graus, {} minutos e {} segundos".format(radF,minF,segF))