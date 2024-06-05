import sys
input = sys.stdin.readline

N = int(input())
word = str(input()).strip()

hidden = '0'
total = 0

for i in range(N):
    if ord(word[i]) <= 57:
        hidden += word[i]
    else:
        total += int(hidden)
        hidden = '0'
        
if(hidden != '0'):
    total += int(hidden)
        
print(total)