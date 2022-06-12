from collections import deque
import sys

test_case = int(sys.stdin.readline()[:-1])
for _ in range(test_case):
    N, M = map(int, sys.stdin.readline()[:-1].split())
    dq = deque(map(int, sys.stdin.readline()[:-1].split()))
    result = 0
    while M>=0:
        dq_max = max(dq)
        while dq_max!=dq[0]:
            dq.append(dq.popleft())
            M-=1
            if M==-1:
                M=len(dq)-1
        dq.popleft()
        M-=1
        result+=1
    print(result)
