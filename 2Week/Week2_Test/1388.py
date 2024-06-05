import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(str, ' '.join(input().split()))))
    
rowCheck = '-'
colCheck = '|'
totalWood = 0

def GetCount():
    global totalWood
    sameColumWoodCount = 0
    
    for row in range(N):
        woodInRow = M
        for col in range(M-1):
            if graph[row][col] == rowCheck and graph[row][col + 1] == rowCheck:
                woodInRow -= 1
                
        totalWood += woodInRow
        
    for col in range(M):
        for row in range(N-1):
            if graph[row][col] == colCheck and graph[row+1][col] == colCheck:
                sameColumWoodCount += 1
                
    return totalWood - sameColumWoodCount

print(GetCount())