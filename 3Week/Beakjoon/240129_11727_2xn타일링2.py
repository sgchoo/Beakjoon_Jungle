import sys
input = sys.stdin.readline

N = int(input())

# solution

resultValue = [0] * 1001

resultValue[0] = 1
resultValue[1] = 1
resultValue[2] = 3


def SquareCount(n):
    global resultValue
    
    if n <= 2:
        print(resultValue[n])
        return
    
    for i in range(3, n+1):
        resultValue[i] = (resultValue[i-1] + resultValue[i-2] + resultValue[i-2]) % 10007
        
    print(resultValue[n] % 10007)
    
SquareCount(N)


# ---------------------------------------------------------------------------------------

# resultValue = [0] * 1001

# resultValue[0] = 1
# resultValue[1] = 1
# resultValue[2] = 3


# def SquareCount(n):
#     global resultValue
    
#     if n <= 2:
#         print(resultValue[n])
#         return
    
#     for i in range(3, n+1):
#         resultValue[i] = resultValue[i-1] + resultValue[i-2] + resultValue[i-3]
        
#     print(resultValue[n])
    
# SquareCount(N)