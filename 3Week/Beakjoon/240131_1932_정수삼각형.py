import sys
input = sys.stdin.readline

triangleSize = int(input())

dp = [[None] for _ in range(triangleSize)]

for i in range(triangleSize):
    dp[i] = list(map(int, input().split()))
    
for i in range(triangleSize-2, -1, -1):
    for j in range(len(dp[i])):
        dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + dp[i][j]
        
print(*dp[0])