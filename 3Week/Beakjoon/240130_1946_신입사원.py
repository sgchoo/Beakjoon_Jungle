import sys
import heapq
input = sys.stdin.readline

T = int(input())

def GetPassPeople(list):
    junior = 1
    que = list
    stdResult1, stdResult2 = heapq.heappop(que)
    
    while que:
        nextResult1, nextResult2 = heapq.heappop(que)
        if nextResult2 < stdResult2:
            stdResult1, stdResult2 = nextResult1, nextResult2
            junior += 1
            
    return junior


for _ in range(T):
    people = int(input())
    examResults = []
    for _ in range(people):
        exam1, exam2 = map(int, input().split())
        heapq.heappush(examResults, (exam1, exam2))
    
    print(GetPassPeople(examResults))