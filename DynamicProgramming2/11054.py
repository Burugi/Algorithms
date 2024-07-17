def longest_bitonic_subsequence(arr):
    n = len(arr)
    
    dp_inc = [1] * n
    dp_dec = [1] * n
    
    # 증가 부분 수열 계산
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)
    
    # 감소 부분 수열 계산
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                dp_dec[i] = max(dp_dec[i], dp_dec[j] + 1)
    
    # 가장 긴 바이토닉 부분 수열 계산
    max_len = 0
    for i in range(n):
        max_len = max(max_len, dp_inc[i] + dp_dec[i] - 1)
    
    return max_len

# 입력 처리
n = int(input())
arr = list(map(int, input().split()))
print(longest_bitonic_subsequence(arr))
