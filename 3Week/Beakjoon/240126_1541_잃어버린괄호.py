import sys
input = sys.stdin.readline

# solution

temp = input().split('-')

list = []

for i in temp:
    sum = 0
    addNum = i.split('+')
    for j in addNum:
        sum += int(j)
    list.append(sum)
    
n = list[0]

for i in range(1, len(list)):
    n -= list[i]
print(n)