from collections import deque
import sys
input = sys.stdin.readline

field = int(input())

cnt = 1

def GetVegitableArea(que: deque, area: list):
    global cnt
    tempX, tempY = que[0]
    
    area[tempX][tempY] += cnt
    
    while que:
        curX, curY = que.popleft()
        
        dirX = [1, -1, 0, 0]
        dirY = [0, 0, 1, -1]
        
        for i in range(4):
            nextX = curX + dirX[i]
            nextY = curY + dirY[i]
            if 0 <= nextX < colum and 0 <= nextY < row and area[nextX][nextY] == 1:
                que.append((nextX, nextY))
                area[nextX][nextY] += cnt
                
    cnt += 1

for _ in range(field):
    vegiQue = deque()
    row, colum, count = map(int, input().split())
    graph = [[0 for _ in range(row)] for _ in range(colum)]
    
    for _ in range(count):
        y, x = map(int, input().split())
        graph[x][y] = 1
        
    for x in range(colum):
        for y in range(row):
            if graph[x][y] == 1:
                vegiQue.append((x, y))
                GetVegitableArea(vegiQue, graph)
                
    print(cnt - 1)
    cnt = 1
    
    
        