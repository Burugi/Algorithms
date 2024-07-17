def max_path_sum(triangle):
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]
    
    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])

    return max(dp[n-1])

# 입력 처리
n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
print(max_path_sum(triangle))
