N = int(input())
T, P=[],[]

# 다이나믹 프로그래밍에 관해서 글을 써야겠다.
def solve(N,T,P):
    dp=[0]*(N+1)
    
    for i in range(N):
        if dp[i]>dp[i+1]:
            dp[i+1]=dp[i]
            
        if i+T[i]<=N:
            dp[i+T[i]]=max(dp[i+T[i]],dp[i]+P[i])
            
    return dp[N]

for _ in range(N):
    t,p=map(int,input().split())
    T.append(t)
    P.append(p)
    
print(solve(N,T,P))