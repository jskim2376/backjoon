n = int(input())
count = 0
while n%5>0:
    n-=2
    count +=1
if n<0:
    print(-1)
else:
    print(count + n//5)
    