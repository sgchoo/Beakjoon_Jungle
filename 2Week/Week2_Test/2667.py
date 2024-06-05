import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, ' '.join(input().split()))))
    
list = []
    
def SetHouse(graph, x, y):
    que = deque()
    que.append((x, y))
    graph[x][y] = 0
    count = 1
    
    while que:
        curX, curY = que.popleft()
        
        dirX = [1, -1, 0, 0]
        dirY = [0, 0, 1, -1]
        
        for i in range(4):
            nextX = curX + dirX[i]
            nextY = curY + dirY[i]
            
            if 0 <= nextX < N and 0 <= nextY < N:
                if graph[nextX][nextY] == 1:
                    graph[nextX][nextY] = 0
                    que.append((nextX, nextY))
                    count += 1
                    
    list.append(count)
                    
def FindHouse():
    global graph
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                SetHouse(graph, i, j)
                
FindHouse()

list.sort()
print(len(list))
for i in list:
    print(i)