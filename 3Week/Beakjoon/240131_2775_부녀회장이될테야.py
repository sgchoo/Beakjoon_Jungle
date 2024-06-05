import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    floor = int(input())
    unit = int(input())
    dp = [[1 for _ in range(unit)] for _ in range(floor+1)]
    
    for i in range(1, unit+1):
        dp[0][i-1] = i   
    
    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
    print(dp[floor][unit-1])