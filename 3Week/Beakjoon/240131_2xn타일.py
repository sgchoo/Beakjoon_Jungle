import sys
input = sys.stdin.readline

T = int(input())

dp = [1] * 1001
dp[2] = 2

def PrintCount(num):
    global dp
    
    if num <= 2:
        print(dp[num] % 10007)
        return
    
    for i in range(3, num+1):
        dp[i] = dp[i-1] + dp[i-2]
        
    print(dp[num] % 10007)
    
PrintCount(T)