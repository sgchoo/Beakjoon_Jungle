import sys
input = sys.stdin.readline

number = int(input())

dp = [0 for _ in range(number + 1)]

def PinaryNumber(num):
    global dp
    
    if num <= 1:
        print(num)
        return
    elif num == 2:
        print(1)
        return
    
    dp[1] = 1
    dp[2] = 1
    
    for i in range(3, num+1):
        dp[i] = dp[i-1] + dp[i-2]
        
    print(dp[num])
    
PinaryNumber(number)