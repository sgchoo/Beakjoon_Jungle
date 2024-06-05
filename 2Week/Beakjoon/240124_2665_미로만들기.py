import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, ' '.join(input().split())))
   

# ---------------------------------------------------------------------------------
# 메모리 초과
    
# pathList = []
# blockList = [(0, 0)]
# changeBlock = 0
    
# def GetMinDistance(list):
#     # global blockList
#     global changeBlock
    
#     que = deque()
#     blockQue = deque()
#     temp = []
    
#     for i in range(len(list)):
#         x, y = list[i]
#         que.append((x,y))
        
#     graph[0][0] += 1
    
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
    
#     while que:
#         # print(que)
#         curX, curY = que.popleft()
#         blockQue.clear()
        
#         for i in range(4):
#             nx = curX+dx[i]
#             ny = curY+dy[i]
            
#             if nx >= N or nx < 0 or ny >= N or ny < 0:
#                 continue
            
#             # print(f'if문 뒤 {nx} {ny}: {graph[nx][ny]}')
            
#             if nx == N-1 and ny == N-1:
#                 return
            
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] += 1
#                 que.append((nx, ny))
#             elif graph[nx][ny] == 0:
#                 blockQue.append((nx, ny))
    
#     for _ in range(len(blockQue)):
#         blockX, blockY = blockQue.popleft()
#         temp.append((blockX, blockY))
#     changeBlock += 1
#     GetMinDistance(temp)
                
# GetMinDistance(blockList)
# print(changeBlock if changeBlock > 0 else 0)