import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split(' '))

graph = [[] for _ in range(N + 1)]
dfsVisited = [False for _ in range(N + 1)]
bfsVisited = [False for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)
    
for i in graph:
    i.sort()

def Dfs(list: list, start: int, visited: list):
    visited[start] = True
    print(start, end=' ')
    
    for i in list[start]:
        if not visited[i]:
            visited[i] = True
            Dfs(list, i, visited)

def Bfs(list: list, start: int, visited: list):
    que = deque([start])
    
    while que:
        cur = que.popleft()
        
        if not visited[cur]:
            visited[cur] = True
            print(cur, end=' ')
            que.extend(list[cur])
            
Dfs(graph, V, dfsVisited)
print()
Bfs(graph, V, bfsVisited)