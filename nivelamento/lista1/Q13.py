q = float(input())
i = float(input())

tempo = q / i 
tempoF = tempo * 60

if tempoF >= 72:
    print(round(tempoF,1))
    print("suporta o ataque")
else:
    print(round(tempoF,1))
    print("nao suporta o ataque")    