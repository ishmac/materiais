n = int(input())
total = 0

for i in range(n):
    num = float(input())
    total += num

media = total / n
print(round(media,2))