import sys
input = sys.stdin.read
MOD = 1000000000 # MOD에서 0이 하나 빠져있었다.
def count_stair_num(n):
    dp=[[0]*10 for _ in range(n+1)]
    
    for j in range(1,10):
        dp[1][j]=1
        
    for i in range(2,n+1):
        for j in range(10):
            if j>0:
                dp[i][j]+=dp[i-1][j-1]
            if j<9:
                dp[i][j]+=dp[i-1][j+1]
            dp[i][j]%=MOD
    result = sum(dp[n])%MOD
    return result
    
N = int(input().strip())
print(count_stair_num(N))