import math
def standard_deviation(args):
    averege=sum(args)/len(args)
    sd=0
    for i in args:
        sd+=math.pow(i-averege,2)
    return math.sqrt(sd/len(args))

N,K = map(int,input().split())
args = list(map(int,input().split()))
minSd=math.inf

for i in range(0,N-K+1):
    for j in range(K+i,N+1):
       sd=standard_deviation(args[i:j])
       minSd = sd if minSd>sd else minSd
print(minSd)
