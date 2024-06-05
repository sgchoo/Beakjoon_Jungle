import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# Solution
visit = [0] * (N+1)

def FindParent(start):
    for i in graph[start]:
        if not visit[i]:
            visit[i] = start
            FindParent(i)
           
FindParent(1)

for i in range(2, N+1):
    print(visit[i])

# -------------------------------------------------------
# 시간 초과

# def FindParent(start, count):
#     checkCount = count
#     visit[start] = True
#     if checkCount > 1:
#         return
    
#     for i in graph[start]:
#         if not visit[i]:
#             print(i)
#             return

#         FindParent(i, count+1)
        
# for j in range(2, N+1):
#     visit = [False] * (N+1)
#     FindParent(j, 0)