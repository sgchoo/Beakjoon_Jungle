import heapq
import sys
input = sys.stdin.readline

heap = []
classRoom = []

N = int(input())
for _ in range(N):
    num, startTime, endTime = map(int, input().split())
    heapq.heappush(heap, (startTime, endTime))
    
start, end = heapq.heappop(heap)
heapq.heappush(classRoom, end)

while heap:
    start, end = heapq.heappop(heap)
    if classRoom[0] <= start:
        heapq.heappop(classRoom)
    heapq.heappush(classRoom, end)
    
print(len(classRoom))