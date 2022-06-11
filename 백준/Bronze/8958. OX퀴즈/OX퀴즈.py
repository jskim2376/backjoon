testCount = int(input())

for i in range(testCount):
	oxList = input()
	totalScore=0
	score=1
	for k in range(len(oxList)):
		if oxList[k]=="O":
			totalScore+=score
			score+=1
		else:
			score=1
	print(totalScore)