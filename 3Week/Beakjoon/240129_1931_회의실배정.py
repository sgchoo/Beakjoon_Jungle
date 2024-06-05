import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())

import heapq

list = []

for i in range(N):
    start, end = map(int, input().split())
    heapq.heappush(list, (end, start))
    
count = 0
    
def Count():
    global count
    firstEnd, firstStart = heapq.heappop(list)
    count += 1
    
    while list:
        endTime, startTime = heapq.heappop(list)
        
        if firstEnd <= startTime:
            firstEnd = endTime
            count += 1
        
Count()
print(count)

# -----------------------------------------------------

# 메모리 초과

# list = [None] * N

# for i in range(N):
#     start, end = map(int, input().split())
#     list[i] = (end, start)
    
# count = 0
# list.sort()

# def Count(n):
#     global count
#     count += 1
#     first = list[n][0]
#     for i in range(n, N):
#         if first <= list[i][1]:
#             return Count(i)
        
# Count(0)
# print(count)


# ------------------------------------------------------------

# import heapq
# list = []

# for i in range(N):
#     start, end = map(int, input().split())
#     heapq.heappush(list, (end, start))
    
# count = 0

# def Count(n):
#     global count
#     count += 1
#     first = list[n][0]
#     for i in range(n, N):
#         if first <= list[i][1]:
#             return Count(i)
        
# Count(0)
# print(count)