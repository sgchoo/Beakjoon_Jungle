import sys
input = sys.stdin.readline

string1 = input().rstrip()
string2 = input().rstrip()
string3 = input().rstrip()

S1 = len(string1)
S2 = len(string2)
S3 = len(string3)

dp = [[[0 for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)] for _ in range(len(string3) + 1)]

for i in range(1, S1+1):
    for j in range(1, S2+1):
        for k in range(1, S3+1):
            if string1[i-1] == string2[j-1] and string2[j-1] == string3[k-1]:
                dp[k][i][j] = dp[k-1][i-1][j-1] + 1
                
            else:
                dp[k][i][j] = max(dp[k-1][i][j], dp[k][i-1][j], dp[k][i][j-1])
                    
print(dp[S3][S1][S2])