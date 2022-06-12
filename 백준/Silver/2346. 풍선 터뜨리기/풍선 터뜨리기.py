import sys
bullun_count = int(sys.stdin.readline()[:-1])
bullun = list(map(int, sys.stdin.readline()[:-1].split()))
bullun_ordinary = [i for i in range(1, bullun_count+1)]

current_bullun = 0
for _ in range(bullun_count-1):
    bullun_index_move = bullun[current_bullun]    
    if bullun_index_move>0:
        next_bullun = (current_bullun+bullun_index_move-1)%(len(bullun)-1)
    else:
        next_bullun = (current_bullun+bullun_index_move)%(len(bullun)-1)
    bullun.pop(current_bullun)
    print(bullun_ordinary.pop(current_bullun))
    current_bullun=next_bullun
print(bullun_ordinary.pop())
