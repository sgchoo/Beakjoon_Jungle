import sys
from collections import deque
input = sys.stdin.readline

array = list(input().strip())
stringQue = []
# temp_que = deque(array)

boom = list(input().strip())
count = 0

for i in array:
    stringQue.append(i)
    if stringQue[len(stringQue) - len(boom):len(stringQue)] == boom:
        for _ in range(len(boom)):
            stringQue.pop()
            
if len(stringQue) == 0:
    print("FRULA")
else:
    print("".join(stringQue))