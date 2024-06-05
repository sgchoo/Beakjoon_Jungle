import sys
input = sys.stdin.readline

N = int(input())

ROUTE = str(input().strip())

outside = []
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for i in ROUTE:
    if i == 0:
        outside.append(i)
    
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def Dfs(start: int, cnt: int):
    visited[start] = True
    
    for i in graph[start]:
        if not visited[i]:
            if i in outside:
                visited[i] = True
                Dfs(i, cnt)
            else:
                print('!!!!!!')
                cnt += 1

Dfs(1, count)
print(count)