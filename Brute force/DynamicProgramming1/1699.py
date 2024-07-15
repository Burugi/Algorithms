import sys
input =sys.stdin.read

def sqaure_min_sum(n):
    dp=[0]*(n+1)
    
    for i in range(1,n+1):
        dp[i]=i
        j=1
        while j*j<=i: # 여기에 등호를 안써서 틀렸었음 
            dp[i]=min(dp[i],dp[i-j*j]+1)
            j+=1
    
    return dp[n]

N=int(input().strip())

print(sqaure_min_sum(N))