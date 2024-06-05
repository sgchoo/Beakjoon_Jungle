import sys
input = sys.stdin.readline

V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
parent = [0] * (V+1)
for i in range(1, V+1):
    parent[i] = i

def FindParent(num):
    if parent[num] != num:
        parent[num] = FindParent(parent[num])
    return parent[num]

def Union(v1, v2):
    v1 = FindParent(v1)
    v2 = FindParent(v2)
    
    if parent[v1] != parent[v2]:
        if v1 > v2:
            parent[v1] = v2
        else:
            parent[v2] = v1
            
for i in range(1, len(graph)):
    for j in graph[i]:
        if parent[i] != parent[j]:
            Union(i, j)
            
parent.sort()
checkNum = parent[0]
count = 0
for i in range(len(parent)):
    if checkNum != parent[i]:
        checkNum = parent[i]
        count += 1
        
print(count)