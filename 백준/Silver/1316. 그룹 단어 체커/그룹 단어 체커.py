N=int(input())

for i in range(N):
	word = input()
	inconsistency = False
	
	for j in range(len(word)):
		for k in range(j+1,len(word)):
			if word[j] == word[k] and word[k-1] != word[j]:
				inconsistency=True
	if inconsistency:
		N-=1
print(N)