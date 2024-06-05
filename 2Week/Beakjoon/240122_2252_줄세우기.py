import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
inDegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1
    
def TopologySort():
    result = []
    que = deque()
    for i in range(1, len(inDegree)):
        if inDegree[i] <= 0:
            que.append(i)
            
    while que:
        start = que.popleft()
        result.append(start)
        
        for i in graph[start]:
            inDegree[i] -= 1
            if inDegree[i] <= 0:
                que.append(i)
                
    return result

print(*TopologySort())
