import sys
N, K = map(int, sys.stdin.readline()[:-1].split())
table = [i for i in range(1,N+1)]
result = []
k=0
for n in reversed(range(1, N+1)):
    k+=K-1
    while k>=n:
        k=k%n
    result.append(str(table.pop(k)))
print("<"+", ".join(result)+">")