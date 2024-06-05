import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N-1):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

def Dfs(node: int):
    for i in graph[node]:
        if visited[i] == 0:
            visited[i] = node
            Dfs(i)
            
def Bfs(node: int):
    que = deque([node])
    
    while que:
        cur = que.popleft()
        
        for i in graph[cur]:
            if visited[i] == 0:
                visited[i] = cur
                que.append(i)
            
Bfs(1)

for i in range(2, N + 1):
    print(visited[i])