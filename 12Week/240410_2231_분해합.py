import sys
input = sys.stdin.readline

NUM = int(input())

new = []

for i in range(1, NUM+1):
    if(i == NUM):
        print(0)
        break
    
    sumElem = sum(map(int, str(i)))
    newNum = i + sumElem
    if(newNum == NUM):
        print(i)
        break
    