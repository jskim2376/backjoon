N = int(input())
if N==1:
    print(1)
else:
    num = 2
    while True:
        if ((num+1)* num / 2) > N:
            num-=1
            break
        num+=1
    print(num)