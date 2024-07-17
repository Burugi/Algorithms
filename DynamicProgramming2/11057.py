MOD=10007
def count_way(n):
    dp = [[0]*10 for _ in range(n+1)]
    
    for k in range(10):
        dp[1][k]=1
    
    for i in range(2,n+1):
        for k in range(10):
            dp[i][k]=sum(dp[i-1][j] for j in range(k+1))%MOD
        
    return sum(dp[n][k] for k in range(10))%MOD

n = int(input())
print(count_way(n))