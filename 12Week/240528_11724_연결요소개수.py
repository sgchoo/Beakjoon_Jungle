import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split(' '))

graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
count = 0

for _ in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

def Dfs(list: list, start: int, visited: list):
    visited[start] = True
    
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
            que.extend(list[cur])

for i in range(1, N + 1):
    if not visited[i]:
        if not graph[i]:
            count += 1
            visited[i] = True
        else:
            Bfs(graph, i, visited)
            count += 1
            
print(count)