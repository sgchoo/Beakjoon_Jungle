import sys
import heapq
input = sys.stdin.readline

# solution

N = int(input())

classList = [list(map(int, input().split())) for _ in range(N)]

classList.sort()

que = []
heapq.heappush(que, classList[0][1])

for i in range(1, N):
    if classList[i][0] >= que[0]:
        heapq.heappop(que)
    heapq.heappush(que, classList[i][1])
    
print(len(que))

# ----------------------------------------------------------------

# 시간 초과

# from collections import deque

# classList = []

# N = int(input())

# for _ in range(N):
#     start, end = map(int, input().split())
#     classList.append((start, end))
    
# classList.sort()
# que = deque(classList)

# count = 0

# while que:
#     startTime, endTime = que.popleft()
    
#     for i in range(len(que)):
#         if endTime > que[0][0]:
#             a, b = que.popleft()
#             que.append((a,b))
#         else:
#             startTime, endTime = que.popleft()
            
#     count += 1
    
# print(count)