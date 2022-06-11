A=int(input())
B=int(input())
C=int(input())

numCount = [0 for i in range(10)]
multi = A*B*C
while multi != 0:
	numCount[multi%10]+=1
	multi=multi//10
	
for i in range(10):
	print(numCount[i])