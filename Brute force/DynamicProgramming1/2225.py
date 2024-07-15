MOD = 1000000000 # MOD에서 0이 하나 빠져있었다.
def sum_decomposition(n,k):
    dp=[[0]*(n+1) for _ in range(k+1)]
    for j in range(n+1):
        dp[1][j]=1
        
    for i in range(2,k+1):
        for j in range(n+1):
            dp[i][j]=dp[i-1][j]
            if j > 0:
                dp[i][j]+=dp[i][j-1]
            
    return dp[k][n]%MOD
    
data = input().strip().split()
N = int(data[0])
K = int(data[1])
print(sum_decomposition(N,K))