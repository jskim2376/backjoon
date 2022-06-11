N = input()
num = int(N)

first=int(num/10)
second=num%10

i=1
while True:
	sum = first+second
	first=second
	second=sum%10
	if num == first*10+second:
		break
	i+=1
	
print(i)