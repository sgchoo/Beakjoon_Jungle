import sys
input = sys.stdin.readline

#solution

N = int(input())
dp = [0 for _ in range(N+1)]

for i in range(2, N+1):
    
    dp[i] = dp[i-1] + 1
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
        
print(dp[N])


# --------------------------------------------------------------------------

# N = int(input())
# result = N
# count = 0

# while result != 1:
#     if result % 3 != 0 or result % 2 != 0:
#         result -= 1
#         count += 1
#         continue
    
#     elif result % 3 == 0:
#         result = (result // 3)
#         count += 1
#         continue
        
#     elif result % 2 == 0:
#         result = (result // 2)
#         count += 1
#         continue
    
# print(count)

