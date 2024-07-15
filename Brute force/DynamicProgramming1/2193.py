import sys
input = sys.stdin.read
# MOD = 1000000000 # MOD에서 0이 하나 빠져있었다.
def count_pinary_num(n):
    dp=[[0]*2 for _ in range(n+1)]
    dp[1][1]=1
        
    for i in range(2,n+1):
        for j in range(2):
            if j==0:
                dp[i][j]+=dp[i-1][j]+dp[i-1][j+1]
            else:
                dp[i][j]+=dp[i-1][j-1]
    result = dp[n][0]+dp[n][1]
    return result
    
N = int(input().strip())
print(count_pinary_num(N))