import sys
input = sys.stdin.readline

N = int(input())
numberList = list(map(int, input().split()))

# solution

dp = [1] * N

for i in range(N):
    for j in range(i):
        if numberList[i] > numberList[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))

# ------------------------------------------------------------
# start = 0
# count = 0

# for i in range(N):
#     for j in range(start, N):
#         if numberList[i] > numberList[j]:
#             start = j
#             count += 1
#             break
        
# print(count)