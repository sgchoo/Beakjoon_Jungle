import sys
input = sys.stdin.readline

V = int(input())
E = int(input())

INF = int(1e9)

graph = [[INF] * (V) for _ in range(V)]

for _ in range(E):
    start, end, cost = map(int, input().split())
    graph[start-1][end-1] = min(graph[start-1][end-1], cost)
    
for i in range(V):
    for j in range(V):
        if i == j:
            graph[i][j] = 0
            
for k in range(V):
    for i in range(V):
        for j in range(V):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
for i in range(V):
    for j in range(V):
        if graph[i][j] == INF:
            graph[i][j] = 0
            print(graph[i][j], end=' ')
            
        else:
            print(graph[i][j], end=' ')
    print()