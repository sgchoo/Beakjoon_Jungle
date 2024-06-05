import sys
input = sys.stdin.readline

A, B = map(int, input().split(' '))

listA = list(map(int, input().split(' ')))
listB = list(map(int, input().split(' ')))

for i in listB:
    listA.append(i)

sortList = sorted(listA)
print(*sortList)