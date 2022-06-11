N = int(input())

for i in range(N):
	data=input()
	data=data.split()
	scoreCount=int(data[0])
	average=0

	for j in range(0, scoreCount):
		average=average+int(data[j+1])
		
	average=average/scoreCount
	rate=0
	
	for j in range(0,scoreCount):
		if int(data[j+1])>average:
			rate+=1
	print("%0.3f%%" % (rate/scoreCount*100))