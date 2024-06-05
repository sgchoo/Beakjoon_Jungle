import sys
input = sys.stdin.readline

N = int(input())

# Solution

resultValue = [0] * 11

resultValue[0] = 0
resultValue[1] = 1
resultValue[2] = 2
resultValue[3] = 4

def SumCount(n):
    global resultValue
    
    if n <= 3:
        print(resultValue[n])
        return
    
    for i in range(4, n+1):
        resultValue[i] = resultValue[i-1] + resultValue[i-2] + resultValue[i-3]
        
    print(resultValue[n])
        

for _ in range(N):
    target = int(input())
    SumCount(target)

# ------------------------------------------------------------

# increaseValue = [0] * 11
# resultValue = [0] * 11

# increaseValue[0] = 0
# increaseValue[1] = 1
# increaseValue[2] = 2
# resultValue[0] = 0
# resultValue[1] = 0
# resultValue[2] = 1

# def SumCount(n):
#     global increaseValue
#     global resultValue
    
#     if n <= 2:
#         print(resultValue[n])
#         return
    
#     for i in range(3, n+1):
#         increaseValue[i] = increaseValue[i-1] + 2
#         resultValue[i] = resultValue[i-1] + increaseValue[i-1]
    
#     print(resultValue[n])
        

# for _ in range(N):
#     target = int(input())
#     SumCount(target)