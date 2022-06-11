N=int(input())
mod=N%5
count=int(N/5)

if N==4 or N==7:
 count=-1
elif mod==1 or mod==3:
 count+=1
elif mod==2 or mod==4:
 count+=2
print(count)