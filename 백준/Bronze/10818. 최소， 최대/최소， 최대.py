N  = int(input())
array = map(int, input().split())

minNumber = 1000001
maxNumber = -1000001
for number in array:
    if minNumber > number:
        minNumber = number
    if maxNumber < number:
        maxNumber = number
print(minNumber, maxNumber)