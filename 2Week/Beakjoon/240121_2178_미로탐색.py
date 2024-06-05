import sys
from collections import deque
input = sys.stdin.readline

# DFS

# def FindRoad(v1, v2):
#     global moveCount
#     global moveCheck
#     if 0 <= v1 <= (N-1) and 0 <= v2 <= (M-1):
        
#         if graph[v1][v2] != moveCheck:
#             return
        
#         graph[v1][v2] += 1
#         moveCount += 1
        
#         FindRoad(v1+1, v2)
#         FindRoad(v1-1, v2)
#         FindRoad(v1, v2+1)
#         FindRoad(v1, v2-1)
        
#         if v1 == N-1 and v2 == M-1:
#             print(moveCount)
#             return

# ---------------------------------------------------------------------------------------

# BFS

N, M = map(int, input().split())

graph = [list(map(int, ' '.join(input().split()))) for _ in range(N)]

moveCheck = graph[0][0]

moveCount = 0

def BFS(v1, v2):
    global moveCount
    global moveCheck
    que = deque()
    que.append((v1, v2))
    
    upDown = [1, -1, 0, 0]
    leftRight = [0, 0, -1, 1]
    
    while que:
        x,y = que.popleft()
        
        for i in range(4):
            nx = x + upDown[i]
            ny = y + leftRight[i]
            
            if 0 <= nx <= N-1 and 0 <= ny <= M-1:
                if graph[nx][ny] == moveCheck:
                    que.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1
                    
            if nx == N-1 and ny == M-1:
                print(graph[nx][ny])
                return
            
BFS(0,0)