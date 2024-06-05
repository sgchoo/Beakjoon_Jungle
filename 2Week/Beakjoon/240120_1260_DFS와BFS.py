import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs_recursion(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    graph[start].sort()
    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs_recursion(graph, i, visited)
            
def dfs_stack(graph, start, visited):
    stack = []
    stack.append(start)
    
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            print(current, end=' ')
            graph[current].sort()
            stack.extend(reversed(graph[current]))
            
def bfs_queue(graph, start, visited):
    que = deque([start])
    que.append(start)
    
    while que:
        current = que.popleft()
        
        if not visited[current]:
            visited[current] = True
            print(current, end=' ')
            graph[current].sort()
            que.extend(graph[current])
            
visited = [False] * (N+1)
# dfs_recursion(graph, V, visited)
dfs_stack(graph, V, visited)
print()
visited = [False] * (N+1)
bfs_queue(graph, V, visited)
