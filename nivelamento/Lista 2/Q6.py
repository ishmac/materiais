texto = input()
l1, l2= input().split(' ')
result = ''
for i in texto:
        if i == l1:
                i = l2
        result += i
print (result)
