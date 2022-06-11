S = input()
S = S.upper()
alpabet = [0 for i in range(26)]

for i in range(len(S)):
	alpabet[ord(S[i])-65] +=1

best = 0
same = False
for i in range(1,26):
	if alpabet[best] < alpabet[i]:
		best=i
		same=False
	elif alpabet[best] == alpabet[i]:
		same=True
if same:
	print('?')
else:
	print(chr(best+65))