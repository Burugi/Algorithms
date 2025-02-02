n = int(input())

# 
def build_block(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=3
    
    for i in range(3,n+1):
        dp[i]=(dp[i-1]+dp[i-2]*2)%10007
        
    return dp[n]

print(build_block(n)%10007)