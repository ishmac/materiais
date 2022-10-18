popA = int(input())
popB = int(input())
anos = 0

while popA < popB:
    popA = (popA + (popA * 0.03))
    popB = (popB + (popB * 0.015))
    print(int(popA), int(popB))
    anos += 1
print(anos)