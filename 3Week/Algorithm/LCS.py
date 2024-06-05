def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    # DP 테이블 초기화
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # DP 테이블 채우기
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # LCS 길이 반환
    return dp[m][n]

# 예시 사용
X = "ABCBDAB"
Y = "BDCAB"
result = longest_common_subsequence(X, Y)
print("Longest Common Subsequence의 길이:", result)