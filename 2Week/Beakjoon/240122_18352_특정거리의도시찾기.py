# 다익스트라 사용

import sys
import heapq
input = sys.stdin.readline

N, M, K, start = map(int, input().split())

INF = int(1e9)
distance = [INF] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
  
def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    
    while heap:
        dist, node = heapq.heappop(heap)
        if distance[node] < dist:
            continue
        for i in graph[node]:
            cost = distance[node]+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
                
dijkstra(start)

count = 0
for i in range(1, N+1):
    if distance[i] == K:
        count += 1
        print(i)
if count <= 0:
    print(-1)