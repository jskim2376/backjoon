S = input()
alpabet = [-1 for i in range(26)]
for i in range(len(S)):
	index=ord(S[i])-97
	if alpabet[index] == -1:
		alpabet[index]=i
for i in range(26):
	print(f'{alpabet[i]} ', end="")