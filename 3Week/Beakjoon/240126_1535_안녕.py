# import sys
# input = sys.stdin.readline

# Solution

# N = int(input())
# healthList = list(map(int, input().split()))
# pleasureList = list(map(int, input().split()))

# pleasure = [0 for _ in range(101)]

# for i in range(1, N+1):
#     h = healthList[i-1]
#     p = pleasureList[i-1]
    
#     for j in range(100, h-1, -1):
#         pleasure[j] = max(pleasure[j], p + pleasure[j-1])
        
# print(pleasure[100])


# --------------------------------------------------------------------

import sys
input = sys.stdin.readline

N = int(input())
healthList = list(map(int, input().split()))
pleasureList = list(map(int, input().split()))

getPleasure = [0] * 101

tempList = []

for i in range(N):
    health = healthList[i]
    pleasure = pleasureList[i]
    tempList.append((health, pleasure))
    
for greeting in tempList:
    h, p = greeting

    for i in range(100, h-1, -1):
        if i >= h:
            getPleasure[i] = max(getPleasure[i], getPleasure[i-h]+p)
            
print(getPleasure[99])