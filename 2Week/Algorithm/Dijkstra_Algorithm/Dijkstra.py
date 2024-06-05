# 순차 탐색

import sys
input = sys.stdin.readline

INF = int(1e9)                              # 무한을 의미하는 값으로 10억을 설정

v, e = map(int, input().split())            # 노드, 간선 갯수 입력받기

start = int(input())                        # 시작 노드 번호를 입력받기
graph = [[] for i in range(v+1)]            # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
visited = [False] * (v+1)                   # 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
distance = [INF] * (v+1)                    # 최단 거리 테이블을 모두 무한으로 초기화

# 모든 간선 정보를 입력받기
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))                 # a번 노드에서 b번 노드로 가는 비용이 c
    
# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def GetSmallestNode():
    minValue = INF
    index = 0                               # 가장 최단 거리가 짧은 노드(인덱스)
    
    for i in range(1, v+1):
        if distance[i] < minValue and not visited[i]:
            minValue = distance[i]
            index = i
    
    return index


def Dijkstra(start):
    distance[start] = 0
    visited[start] = True
    
    # 시작 노드에 대한 초기화
    for i in graph[start]:
        distance[i[0]] = i[1]
        
    # 시작 노드를 제외한 전체 (v-1)개의 노드에 대해 반복
    for i in range(v-1):
        now = GetSmallestNode()             # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
        visited[now] = True
        
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost > distance[j[0]]:
                distance[j[0]] = cost
                
                
Dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
        
        
# -----------------------------------------------------------------------------------------------------------------
# 우선순위 큐
import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())
INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append(b, c)
    
def Dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))                   # 시작 노드 정보 우선순위 큐에 삽임
    distance[start] = 0                             # 시작 노드 -> 시작 노드 거리 기록
    
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:                   # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우(=방문 완료) 무시
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]         # 시작 -> node 거리 + node->node의 인접 노드 거리
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
                
Dijkstra(start)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print('도달할 수 없음')
    else:
        print(distance[i])