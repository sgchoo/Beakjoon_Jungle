import sys
input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

maxValue = int(-1e9)
minValue = int(1e9)

def GetValue(count: int, result: int):
    global add, sub, mul, div, maxValue, minValue

    if count == N:
        maxValue = max(maxValue, int(result))
        minValue = min(minValue, int(result))
        
    else:
        if add > 0:
            add -= 1
            GetValue(count + 1, result + numList[count])
            add += 1
        if sub > 0:
            sub -= 1
            GetValue(count + 1, result - numList[count])
            sub += 1
        if mul > 0:
            mul -= 1
            GetValue(count + 1, result * numList[count])
            mul += 1
        if div > 0:
            div -= 1
            GetValue(count + 1, int(result / numList[count]))
            div += 1
            
GetValue(1, numList[0])

print(maxValue)
print(minValue)