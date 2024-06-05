import sys
import heapq
input = sys.stdin.readline

classRoom = int(input())

heap = []

for _ in range(classRoom):
    classNum, startTime, endTime = map(int, input().split())
    heapq.heappush(heap, (endTime, startTime, classNum))