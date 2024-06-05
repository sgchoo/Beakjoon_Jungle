import sys
input = sys.stdin.readline

N = str(input()).strip()
sum = 0

if(N[0] == '0' and N[1] == 'x'):
    for i in range(len(N) - 1, 1, -1):
        if(N[i] == 'a'):
            sum += 10 * 16**(len(N) - (i+1))
        elif(N[i] == 'b'):
            sum += 11 * 16**(len(N) - (i+1))
        elif(N[i] == 'c'):
            sum += 12 * 16**(len(N) - (i+1))
        elif(N[i] == 'd'):
            sum += 13 * 16**(len(N) - (i+1))
        elif(N[i] == 'e'):
            sum += 14 * 16**(len(N) - (i+1))
        elif(N[i] == 'f'):
            sum += 15 * 16**(len(N) - (i+1))
        else:
            sum += int(N[i]) * 16**(len(N) - (i+1))
            
    print(sum)
elif(N[0] == '0'):
    for i in range(len(N) - 1, 0, -1):
        sum += int(N[i]) * 8**(len(N) - (i+1))
    print(sum)
else:
    print(N)