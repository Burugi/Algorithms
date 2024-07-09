n = int(input())
prices=list(map(int,input().split()))

def max_prices(n,prices):
    dp=[0]*(n+1)
    
    for i in range(1,n+1):
        for j in range(1,i+1):
            dp[i]=max(dp[i],dp[i-j]+prices[j-1])
    
    return dp[n]
print(max_prices(n,prices))