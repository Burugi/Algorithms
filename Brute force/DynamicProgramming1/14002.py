import sys
input =sys.stdin.read

def LIS(n,a):
    dp=[1]*n
    prev=[-1]*n
    
    for i in range(1,n):
        for j in range(i):
            if a[i]>a[j]and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    prev[i]=j
    length=max(dp)
    lis_index=dp.index(length)
    lis_list=[]
    while lis_index!=-1:
        lis_list.append(a[lis_index])
        lis_index=prev[lis_index]
    
    lis_list.reverse()
    return length, lis_list

data=input().strip().split()
N=int(data[0])
A=list(map(int,data[1:]))

length, lis_list=LIS(N,A)
print(length)
print(" ".join(map(str,lis_list)))