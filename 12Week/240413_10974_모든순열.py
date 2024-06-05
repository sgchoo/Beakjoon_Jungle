import sys
input = sys.stdin.readline

NUM = int(input())

array = []

def dfs():
    if len(array) == NUM:
        print(*array)
        return
    
    for i in range(1, NUM +1):
        if i not in array:
            array.append(i)
            dfs()
            array.pop()
            
dfs()
