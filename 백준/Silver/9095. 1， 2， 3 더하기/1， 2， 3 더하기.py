from math import factorial
import sys
dp = [0 for i in range(12)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

count = int(sys.stdin.readline())

for c in range(count):
    n = int(sys.stdin.readline())
    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])