import sys
from collections import deque
input = sys.stdin.readline

Y, X, Z = map(int, input().split())

graph = [[] for _ in range(Z)]

for z in range(Z):
    for x in range(X):
        graph[z].append(list(map(int, input().split())))  

spendTime = 0
      
def CheckTomato(graph):
    global spendTime
    que = deque()
    count = 0
            
    for z in range(Z):
        for x in range(X):
            if 0 not in graph[z][x]:
                count +=1
            for y in range(Y):
                if graph[z][x][y] == 1:
                    que.append((z, x, y))
                    
    if count == (X*Z):
        print(0)
        return
    
    nx = [0, 0, 1, -1, 0, 0]
    ny = [0, 0, 0, 0, 1, -1]
    nz = [1, -1, 0, 0, 0, 0]
    
    while que:
        for _ in range(len(que)):
            dz, dx, dy = que.popleft()
            for i in range(6):
                curZ = dz + nz[i]
                curX = dx + nx[i]
                curY = dy + ny[i]
                
                if curZ >= Z or curZ < 0 or curX >= X or curX < 0 or curY >= Y or curY < 0:
                    continue
                
                if graph[curZ][curX][curY] == 0:
                    graph[curZ][curX][curY] = 1
                    que.append((curZ, curX, curY))
            
        spendTime += 1
        
    PossibleToGrow(graph, spendTime)
        
    
        
def PossibleToGrow(graph, spendTime):
    count = 0
    for tray in graph:
        for line in tray:
            if 0 in line:
                print(-1)
                return
            elif 0 not in line:
                count += 1
    
    print(spendTime-1)
      
CheckTomato(graph)
    
# 다익스트라로 구현해보기