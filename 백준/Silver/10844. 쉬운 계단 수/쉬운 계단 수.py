import sys
count = int(sys.stdin.readline())
dp = [[0 for i in range(11)] for c in range(count+1)]
for i in range(1,10): 
    dp[1][i] = 1
for c in range(2,count+1):
    dp[c][0] = dp[c-1][1]
    for i in range(1,10):
        dp[c][i] = dp[c-1][i-1] + dp[c-1][i+1]
print(sum(dp[count]) % 1000000000)