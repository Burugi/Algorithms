def largest_increasing_subsequence(arr):
    n=len(arr)
    dp=[0]*(n)
    
    for i in range(n):
        dp[i]=arr[i]
        for j in range(i):
            if arr[j]<arr[i]:
                dp[i]=max(dp[i],dp[j]+arr[i])
                
    return max(dp)
n=int(input())
arr=list(map(int,input().split()))
print(largest_increasing_subsequence(arr))