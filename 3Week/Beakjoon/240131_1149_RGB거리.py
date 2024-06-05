import sys
input = sys.stdin.readline

N = int(input())

colorCost = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (3) for _ in range(N)]

dp[0] = colorCost[0]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + colorCost[i][j]
        elif j == 1:
            dp[i][j] = min(dp[i-1][0], dp[i-1][2]) + colorCost[i][j]
        elif j == 2:
            dp[i][j] = min(dp[i-1][0], dp[i-1][1]) + colorCost[i][j]
            
print(min(dp[N-1]))