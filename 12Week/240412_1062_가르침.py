import sys
input = sys.stdin.readline

WORD_NUM, WORD_LIMIT = map(int, input().split())

originWord = {'a', 'n', 't', 'i', 'c'}
learningWord = {'a', 'n', 't', 'i', 'c'}
# max = 0

purposeWord = []

for i in range(WORD_NUM):
    purposeWord.append(set(input().strip()))
    
print(max(purposeWord))