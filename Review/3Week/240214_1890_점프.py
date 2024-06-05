import sys
from collections import deque
input = sys.stdin.readline

boardSize = int(input())

dp = [[0 for _ in range(boardSize)] for _ in range(boardSize)]
board = [0 for _ in range(boardSize)]

for i in range(boardSize):
    board[i] = list(map(int, input().split()))
    
dp[0][0] = 1

for x in range(boardSize):
    for y in range(boardSize):
        
        if x == boardSize - 1 and y == boardSize - 1:
            print(dp[x][y])
        
        if y + board[x][y] < boardSize:
            dp[x][y + board[x][y]] += dp[x][y]
            
        if x + board[x][y] < boardSize:
            dp[x + board[x][y]][y] += dp[x][y]
            

# ---------------------------------------------------------------------

# 시간 초과

# boardSize = int(input())

# dp = [[0 for _ in range(boardSize)] for _ in range(boardSize)]
# board = [0 for _ in range(boardSize)]


# for i in range(boardSize):
#     board[i] = list(map(int, input().split()))

# dp[0][0] = 1

# def GetPathCount(start, end):
#     if start == boardSize-1 and end == boardSize-1:
#         dp[start][end] += 1
#         return
#     if not 0 <= start <= boardSize-1 or not 0 <= end <= boardSize-1:
#         return
    
#     GetPathCount(start + board[start][end], end)
#     GetPathCount(start, end + board[start][end])
    
# GetPathCount(0, 0)
    
# print(dp[boardSize-1][boardSize-1])