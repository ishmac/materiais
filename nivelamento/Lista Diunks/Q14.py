eleit = int(input())
d = 0
a = 0 
g = 0 

for i in range(eleit):
    resUser = int(input())
    if resUser == 99:
        d += 1
    elif resUser == 88:
        a += 1
    elif resUser == 77:
        g += 1

print("diunkz: {} / alan: {} / gabriel: {}".format(d,a,g))                