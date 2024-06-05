import sys
input = sys.stdin.readline

string1 = input()
string2 = input()

S1 = [0] * (len(string1))
S2 = [0] * (len(string2))

for i in range(1, len(string1)):
    S1[i] = string1[i-1]
        
for i in range(1, len(string2)):
    S2[i] = string2[i-1]

dp = [[0 for _ in range(len(string2))] for _ in range(len(string1))]

for i in range(1, len(string1)):
    for j in range(1, len(string2)):
        if S1[i] == S2[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
def PrintLcs(xString, yString):
    x, y = len(xString)-1, len(yString)-1
    lcs = []
    
    while x > 0 and y > 0:
        if S1[x] == S2[y]:
            lcs.append(S1[x])
            x -= 1
            y -= 1
            
        elif dp[x-1][y] > dp[x][y-1]:
            x -= 1
            
        else:
            y -= 1
            
    for i in range(len(lcs)-1, -1, -1):
        print(lcs[i], end='')
            
print(dp[len(string1)-1][len(string2)-1])
PrintLcs(string1, string2)
# print(PrintLcs(string1, string2))