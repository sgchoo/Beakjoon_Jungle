import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

numList = [[0] for _ in range(1001)]

temp = list(map(int, input().split()))
heap = []

for i in temp:
    heapq.heappush(heap, i)
    
for _ in range(M):
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    
    sumVal = x+y
    
    x, y = sumVal, sumVal
    
    heapq.heappush(heap, x)
    heapq.heappush(heap, y)
    
print(sum(heap))