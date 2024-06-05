import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

vertex, edge, distance, start = map(int, input().split())

graph = [[] for _ in range(vertex+1)]

for _ in range(edge):
    v, e = map(int, input().split())
    graph[v].append(e)
    
dist = [INF] * (vertex+1)
dist[1] = 0

def Dijkstra(startPos):
    heap = []
    heapq.heappush(heap, (0, startPos))
    
    while heap:
        distance, curPos = heapq.heappop(heap)
        
        if dist[curPos] < distance:
            continue
        cost = distance + 1
        for next in graph[curPos]:
            if dist[next] > cost:
                dist[next] = cost
                heapq.heappush(heap, (cost, next))
                
Dijkstra(start)
count = 0
for i in range(1, len(dist)):
    if dist[i] == distance:
        print(i)
        count += 1
if count <= 0:
    print(-1)