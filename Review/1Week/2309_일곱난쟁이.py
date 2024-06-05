import sys
input = sys.stdin.readline

totalHeight = 0
list = []
for _ in range(9):
    
    a = int(input())
    list.append(a)
    totalHeight += a

check = totalHeight - 100
    
def Find(check):
    for i in range(9):
        for j in range(9):
            if i == j:
                continue
            
            if list[i]+list[j] == check:       
                return list[i], list[j]

a, b = Find(check)

list.remove(a)
list.remove(b)
list.sort()
for i in list:
    print(i)