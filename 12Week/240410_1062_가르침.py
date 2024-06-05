import sys
input = sys.stdin.readline

WORD, STRING = map(int, input().split())

arr = {'a', 'n', 't', 'i', 'c'}
learn = 0


for _ in range(WORD):
    teach_word = set(map(str, input().strip()))
    learn_word = teach_word - arr
    
    if len(arr) < STRING and len(learn_word) > 0:
        for i in range(len(learn_word)):
            temp = list(learn_word)
            arr.add(temp[i])
            
    if len(teach_word - arr) == 0:
        learn += 1
        
print(learn)