num = int(input())
lista = [] 
somaTodos = 0
for i in range(num):
    res = int(input())
    lista.append(res)
    somaTodos += res

if ( somaTodos / 2 ) == lista[1]:
    print(1)
else:
    print(0)    

