import sys
import heapq
input = sys.stdin.readline

T = int(input())

que = []
claasRoom = []

for _ in range(T):
    number, start, end = map(int, input().split())
    heapq.heappush(que, (start, end, number))
    
# 시간 부족으로 못풀었습니다.