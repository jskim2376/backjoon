n=int(input())
locate=n
rowColumn=1
while True:
	if locate<=rowColumn:
		break
	else:
		locate-=rowColumn
		rowColumn+=1
if rowColumn%2:
	print(f"{rowColumn-locate+1}/{locate}")
else:
	print(f"{locate}/{rowColumn-locate+1}")