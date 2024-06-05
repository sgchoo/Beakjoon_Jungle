import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dp = [0 for _ in range(N+1)]

numberList = list(map(int, input().split()))

dp[1] = numberList[0]

for i in range(2, N+1):
    dp[i] = dp[i-1] + numberList[i-1]
        
for _ in range(M):
    a, b = map(int, input().split())
    if a == 1:
        print(dp[b])
    elif a != 1:
        print(dp[b] - dp[a-1])