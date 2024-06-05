import sys
input = sys.stdin.readline

V = int(input())
E = int(input())

graph = [[] for _ in range(V+1)]
inDegree = [0] * (V+1)
neededCost = [0] * (V+1)
basicItem = []

for _ in range(E):
    targetItem, needItem, cost = map(int, input().split())
    graph[targetItem].append((needItem, cost))
    inDegree[needItem] += 1
    
for i in range(1, V+1):
    if not graph[i]:
        basicItem.append(i)
    
def GetBasicItemCount(basicList):
    stack = []
    
    for i in range(1, V+1):
        if inDegree[i] == 0:
            stack.append(i)
            
    for i in stack:
        neededCost[i] = 1
            
    while stack:
        targetItem = stack.pop()
        
        for i in graph[targetItem]:
            need, count = i[0], i[1]
            # if neededCost[targetItem] != 0:
            neededCost[need] = neededCost[need] + (neededCost[targetItem] * count)
            # else:
            #     neededCost[need] = neededCost[need] + count
            inDegree[need] -= 1
            if inDegree[need] <= 0:
                stack.append(need)
                
    for i in basicList:
        print(f'{i} {neededCost[i]}')
        
GetBasicItemCount(basicItem)