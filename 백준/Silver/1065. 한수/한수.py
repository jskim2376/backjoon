def soloNum(n):
	if n<10:
		return True
	elif n<100:
		return True
	else:
		if n//10%10 - n%10 == n//100 - n//10%10:
			return True

N=int(input())
hanCount=0
for i in range(1,N+1):
	if soloNum(i):
		hanCount+=1
print(hanCount)