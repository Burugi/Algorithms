MOD=9901
def min_way(n):
    dp = [[0]*3 for _ in range(n)]
    dp[0][0]=1
    dp[0][1]=1
    dp[0][2]=1
    
    for i in range(1,n):
        dp[i][0]=(dp[i-1][0]+dp[i-1][1]+dp[i-1][2])%MOD
        dp[i][1]=(dp[i-1][0]+dp[i-1][2])%MOD
        dp[i][2]=(dp[i-1][0]+dp[i-1][1])%MOD
        
    return (dp[n-1][0]+dp[n-1][1]+dp[n-1][2])%MOD

n = int(input())
print(min_way(n))