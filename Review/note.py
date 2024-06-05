import sys
input = sys.stdin.readline

bp = [0 for _ in range(8)]
bp[1] = 1
bp[2] = 1
bp[3] = 2

recur = [0 for _ in range(8)]
recur[1] = 1
recur[2] = 1
recur[3] = 2


for i in range(4, 8):
    bp[i] = bp[i-1] + bp[i-2]

for i in range(1, len(bp)):
    print(bp[i])
    
def RecurFivo(idx):
    if idx < 3:
        return
    
    RecurFivo(idx-1)
    recur[idx] = recur[idx-1] + recur[idx-2]
    
RecurFivo(7)
for i in range(1, len(recur)):
    print(recur[i])