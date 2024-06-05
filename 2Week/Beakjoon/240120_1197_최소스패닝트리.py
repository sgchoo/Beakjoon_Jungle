import sys
input = sys.stdin.readline

v, e = map(int,input().split())
parent = [None] * (v+1)

for i in range(1, v+1):
    parent[i] = i
    
def FindParent(target):
    if parent[target] != target:
        parent[target] = FindParent(parent[target])
    return parent[target]

def Union(v1, v2):
    v1 = FindParent(v1)
    v2 = FindParent(v2)
    if parent[v1] != parent[v2]:
        if v1 > v2:
            parent[v1] = v2
        else:
            parent[v2] = v1
        
edges = []
totalCost = 0

for _ in range(e):
    v1, v2, cost = map(int, input().split())
    edges.append((cost, v1, v2))
    
edges.sort()

for i in range(e):
    c, a, b = edges[i]
    
    if FindParent(a) != FindParent(b):
        Union(a, b)
        totalCost += c
        
print(totalCost)