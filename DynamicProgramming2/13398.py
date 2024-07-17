def max_sum(arr):
    n = len(arr)
    if n==1:
        return arr[0]
    
    dp=[[0]*2 for _ in range(n)]
    dp[0][0]=arr[0]
    dp[0][1]=arr[0]
    
    max_sum=arr[0]
    
    for i in range(1,n):
        dp[i][0]=max(dp[i-1][0]+arr[i],arr[i])
        dp[i][1]=max(dp[i-1][1]+arr[i],dp[i-1][0])
        max_sum=max(max_sum,dp[i][0],dp[i][1])
    return max_sum
    

# 입력 처리
n = int(input())
arr = list(map(int, input().split()))
print(max_sum(arr))
