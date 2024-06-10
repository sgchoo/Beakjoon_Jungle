import sys
input = sys.stdin.readline

N = int(input())
ROUTE = str(input().strip())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def Dfs(jogRoute: list, start: int, isVisited: list):
    global count
    isVisited[start] = True
    
    for i in jogRoute[start]:
        if not isVisited[i]:
            if ROUTE[i-1] == '1':
                count += 1
            elif ROUTE[i-1] == '0':
                Dfs(jogRoute, i, isVisited)
                
for i in range(1, N + 1):
    if ROUTE[i-1] != '0':
        Dfs(graph, i, visited)
    visited = [False] * (N + 1)
        
print(count)