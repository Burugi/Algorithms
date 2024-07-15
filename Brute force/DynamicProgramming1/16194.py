n = int(input())
prices=list(map(int,input().split()))

def min_prices(n,prices):
    dp=[float("inf")]*(n+1)
    dp[0]=0 # 이 초기화가 반드시 필요함
    for i in range(1,n+1):
        for j in range(1,i+1):
            dp[i]=min(dp[i],dp[i-j]+prices[j-1])
    
    return dp[n]
print(min_prices(n,prices))