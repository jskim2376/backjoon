from math import factorial
import sys


card_count = int(sys.stdin.readline())
cardpack = list(map(int, sys.stdin.readline().split()))
dp = [0 for i in range(card_count)]
dp[0] = cardpack[0]
dp[1] = max(cardpack[0]+cardpack[0], cardpack[1])

for i in range(2,card_count):
    dp[i] = cardpack[i]
    for j in range(0,i):
        dp[i] = max(dp[i], dp[j]+dp[i-j-1])
print(dp[card_count-1])