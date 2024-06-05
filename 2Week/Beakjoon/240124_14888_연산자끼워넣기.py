import sys
input = sys.stdin.readline

# Solution

# N = int(input())
# graph = list(map(int, input().split()))
    
# add, sub, mult, div = map(int, input().split())

# minValue = int(1e9)
# maxValue = -int(1e9)

# def GetValue(start, result):
#     global add, sub, mult, div, minValue, maxValue
    
#     if start == N:
#         minValue = min(minValue, result)
#         maxValue = max(maxValue, result)
#     else:
#         if add > 0:
#             add -= 1
#             GetValue(start+1, result + graph[start])
#             add += 1
#         if sub > 0:
#             sub -= 1
#             GetValue(start+1, result - graph[start])
#             sub += 1
#         if mult > 0:
#             mult -= 1
#             GetValue(start+1, result * graph[start])
#             mult += 1
#         if div > 0:
#             div -= 1
#             GetValue(start+1, int(result / graph[start]))
#             div += 1

# GetValue(1, graph[0])

# print(maxValue)
# print(minValue)

# ---------------------------------------------------------
# Error

N = int(input())
tempList = list(map(int, input().split()))
add, sub, mult, div = map(int, input().split())
graph = [[] for _ in range(tempList[N-1] + 1)] 
sign = [0, add, sub, mult, div]

for i in range(len(tempList) -1):
    graph[tempList[i]].append(tempList[i+1])

minValue = int(1e9)
maxValue = 0
answer = 1

print(graph)

def GetValue(start, result):
    global minValue
    global maxValue

    if start == graph[N+1][0]:
        minValue = min(minValue, result)
        maxValue = max(maxValue, result)
        
    for i in graph[start]:
        for j in range(1, len(sign)):
            if sign[j] != 0:
                sign[j] -= 1
                
                if j == 1:
                    GetValue(i, result + i)
                elif j == 2:
                    GetValue(i, result - i)
                elif j == 3:
                    GetValue(i, result * i)
                else:
                    if result < 0:
                        GetValue(i, -((-result) // i))
                    else:
                        GetValue(i, result // i)
                sign[j] += 1
                        
                        
GetValue(tempList[0], answer)

print(minValue)
print(maxValue)