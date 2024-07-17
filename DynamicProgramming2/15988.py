MOD = 1000000009

def count_ways(n):
    dp = [0]*(n+1)
    dp[0]=1
    dp[1]=1
    if n>1:
        dp[2]=2
    if n>2:
        dp[3]=4
        
    for i in range(4,n+1):
        dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%MOD
    return dp[n]

t = int(input())
results=[]

for _ in range(t):
    n=int(input())
    results.append(count_ways(n))
    
for result in results:
    print(result)