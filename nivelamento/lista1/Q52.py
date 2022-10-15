tempo = int(input())

#infancia até 1,2 
#adolescencia até 2
#adulto até 7,5
if tempo <= 1.2:
    print("infancia")
elif tempo > 1.2 and tempo <= 2:
    print("adolescencia") 
elif tempo > 2 and tempo <= 7.5:
    print("adulto") 
elif tempo > 7.5:
    print("idoso")          