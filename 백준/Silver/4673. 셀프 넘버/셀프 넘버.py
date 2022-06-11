def d(n):
	return n+int(n%10)+int(n/10%10)+int(n/100%10)+int(n/1000%10)
	
lst=[True for i in range(10000)]

for n in range(1,10000):
	selnum=d(n)
	if selnum<10000:
		lst[selnum]=False
for n in range(1,10000):
	if lst[n]==True:
		print(n)