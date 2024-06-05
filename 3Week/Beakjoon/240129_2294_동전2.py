import sys
input = sys.stdin.readline

Total, target = map(int, input().split())

INF = int(1e9)

coins = [0] * (Total)

for i in range(Total):
    a = int(input())
    coins[i] = a

dp = [INF] * (target + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, target+1):
        dp[i] = min(dp[i], dp[i-coin]+1)
        
if dp[target] == INF:
    print(-1)
else:
    print(dp[target])