import sys
input =sys.stdin.read

def LIS(n,a):
    dp=[1]*n
    
    for i in range(1,n):
        for j in range(i):
            if a[i]>a[j]:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)

data=input().strip().split()
N=int(data[0])
A=list(map(int,data[1:]))

print(LIS(N,A))