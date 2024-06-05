import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
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
            
Dfs(graph, 1, visited)

for i in visited:
    if i:
        count += 1
        
print(count - 1)