import sys
from collections import deque
input = sys.stdin.readline

row, colum = map(int, input().split())

graph = [[] for _ in range(row)]

charPos = ()
waterPos = []
count = 0
arrive = False

for i in range(row):
    route = input().strip()
    for j in range(len(route)):
        graph[i].append(route[j])
        if route[j] == 'S':
            charPos = (i, j)
        elif route[j] == '*':
            waterPos.append((i, j))
    
def WaterMoveInOnce():
    global graph, waterPos
    water = deque()
    
    for i in waterPos:
        water.append(i)
    
    while water:    
        xMove = [1, -1, 0, 0]
        yMove = [0, 0, -1, 1]
        
        curPos = water.popleft()

        for i in range(4):
            nextPos = (curPos[0] + xMove[i], curPos[1] + yMove[i])
            
            if 0 <= nextPos[0] < row and 0 <= nextPos[1] < colum and graph[nextPos[0]][nextPos[1]] == '.':
                graph[nextPos[0]][nextPos[1]] = '*'
                waterPos.append(nextPos)

def CharacterMove():
    global graph, charPos, count, arrive
    
    char = deque()
    char.append(charPos)
    
    while char:
        WaterMoveInOnce()
        
        xMove = [1, -1, 0, 0]
        yMove = [0, 0, -1, 1]
        
        for _ in range(len(char)):
            curPos = char.popleft()
            
            for i in range(4):
                nextPos = (curPos[0] + xMove[i], curPos[1] + yMove[i])
                
                if 0 <= nextPos[0] < row and 0 <= nextPos[1] < colum:
                    if graph[nextPos[0]][nextPos[1]] == '.':
                        char.append(nextPos)
                    elif graph[nextPos[0]][nextPos[1]] == 'D':
                        arrive = True
                    
        count += 1
        if arrive:
            break
                
CharacterMove()

if not arrive:
    print('KAKTUS')
else:
    print(count)