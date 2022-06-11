from math import factorial
import sys
n = int(sys.stdin.readline())
facto = factorial(n)
result = 0
for i in reversed(str(facto)):
    if i != '0':
        print(str(result))
        break
    result+=1