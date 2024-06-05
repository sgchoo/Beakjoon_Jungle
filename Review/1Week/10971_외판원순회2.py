import sys
input = sys.stdin.readline

N = int(input())

cities = [list(map(int, input().split())) for _ in range(N)]
# for i in range(N):
#     cities[i].append(list(map(int, input().split())))
    
visited = [False] * N
visited[0] = True
result = int(1e9)

def GetMinCost(start, count, cost):
    global result
    
    if count == N-1 and cities[start][0] != 0:
        result = min(result, cost + cities[start][0])
        return
    
    for i in range(N):
        if not visited[i] and cities[start][i] != 0:
            visited[i] = True
            GetMinCost(i, count+1, cost+cities[start][i])
            visited[i] = False
            
GetMinCost(0, 0, 0)
print(result)