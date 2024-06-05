import sys
input = sys.stdin.readline

lotto = list(map(int, input().split()))
    
def dfs(array: list, start, end):
    global lotto
    
    if len(array) >= 6:
        print(*array)
        return
    
    for i in range(1, end):
        array.append(lotto[i])
        dfs(array, start+1, end)
        array.pop()

while lotto[0] != 0:
    temp_array = []
    
    dfs(temp_array, 0, len(lotto))
    
    lotto = list(map(int, input().split()))
    