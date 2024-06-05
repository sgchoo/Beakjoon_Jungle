import sys
input = sys.stdin.readline

T = int(input())

dp = [0] * (T+1)

def TileCount(num):
    if num <= 2:
        return num % 15746
    else:
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, num+1):
            dp[i] = (dp[i-1] + dp[i-2]) % 15746
            
        return dp[num] % 15746
    
print(TileCount(T) % 15746)