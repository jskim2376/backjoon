first= int(input())
last= int(input())
arr=[0]*(last+1)
sosu=[0]*(last-first+1)
index=0

cnt=0
sum=0
arr[1]=1 #1꼭 직접 소수 아니라고 표시해주기
for i in range(2,last+1) :
    if arr[i]==0:
        for j in range(i,last+1,i) : 
            arr[j]=1
        arr[i]=0

for i in range(first,last+1) :
    if arr[i]==0:
        sosu[index]=i
        index+=1
        cnt+=1
        sum+=i #합

if cnt == 0 :
    print(-1)
else : 
    print(sum)
    print(sosu[0])