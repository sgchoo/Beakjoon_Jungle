import sys
import heapq
input = sys.stdin.readline

vertex = int(input())
edge = int(input())

INF = int(1e9)

graph = [[] for _ in range(vertex+1)]

for i in range(1, edge+1):
    startNode, endNode, cost = map(int, input().split())
    graph[startNode].append((cost, endNode))
    
start, end = map(int, input().split())
    
distance = [INF] * (vertex + 1)
distance[start] = 0

def GetMinCost(now):
    heap = []
    heapq.heappush(heap, (0, now))
    
    while heap:
        dist, node = heapq.heappop(heap)
        
        if distance[node] < dist:
            continue
        
        for next in graph[node]:
            cost = distance[node] + next[0]
            if distance[next[1]] > cost:
                distance[next[1]] = cost
                heapq.heappush(heap, (cost, next[1]))
                
GetMinCost(start)
print(distance[end])