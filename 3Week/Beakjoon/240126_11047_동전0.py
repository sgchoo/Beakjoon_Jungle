import sys
input = sys.stdin.readline

N, total = map(int, input().split())

coins = []

for _ in range(N):
    coins.append(int(input()))
    
result = 0
def Exchange():
    global result
    global total
    
    for i in range(N-1, -1, -1):
        if total <= 0:
            break
        
        result += total // coins[i]
        total = total % coins[i]
        
Exchange()
print(result)