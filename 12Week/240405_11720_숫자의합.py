import sys
input = sys.stdin.readline

N = int(input())
array = str(input()).strip()
sum = 0

for i in range(N):
    sum += int(array[i])
    
print(sum)