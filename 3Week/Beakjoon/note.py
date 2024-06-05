import sys
input = sys.stdin.readline

T = int(input())

number = list(map(int, input().split()))

dp = [0] * (T)


for i in range(T):
    for j in range(i):
        if number[i] > number[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += number[i]
            
print(max(dp))