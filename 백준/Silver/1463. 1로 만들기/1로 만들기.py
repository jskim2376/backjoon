from math import factorial
import sys
n = int(sys.stdin.readline())
memory = [0 for i in range(n+1)]

for i in range(2,n+1):
    memory[i] = memory[i-1]+1
    if i%2 == 0:
        memory[i] = min(memory[i], memory[i//2]+1)
    if i%3 == 0:
        memory[i] = min(memory[i], memory[i//3]+1)

print(memory[n])