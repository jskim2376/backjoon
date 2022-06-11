count = int(input())
rank=[]
bounty=[]
for count in range(count):
    rank.append(list(map(int,input().split())))
festiv1=[(500,1),(300,3),(200,6),(50,10),(30,15),(10,21)]
festiv2=[(512,1),(256,3),(128,7),(64,15),(32,31)]

for rank1,rank2 in rank:
    totalBounty=0
    for var1, var2 in festiv1:
        if rank1!=0 and rank1<=var2:
            totalBounty+=var1
            break
    for var1, var2 in festiv2:
        if rank2 !=0 and rank2<=var2:
            totalBounty+=var1
            break
    bounty.append(totalBounty*10000)
for i in bounty:
    print(i)