T = int(input().strip())

def count_num(n):
    dp=[0]*(n+1)
    
    dp[0]=1 
    # 0을 표현하는 방법, 아무것도 안넣는 것
    
    for i in range(1,n+1):
        if i>=1:
            dp[i]+=dp[i-1]
        if i>=2:
            dp[i]+=dp[i-2]
        if i>=3:
            dp[i]+=dp[i-3]
    
    return dp[n]

for _ in range(T):
    n=int(input().strip())
    print(count_num(n))