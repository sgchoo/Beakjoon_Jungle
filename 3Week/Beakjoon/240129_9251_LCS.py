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
            
print(dp[len(string1)-1][len(string2)-1])