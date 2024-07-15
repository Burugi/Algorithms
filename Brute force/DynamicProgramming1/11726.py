n = int(input())

# 
def build_block(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    # 위의 if문이 없으면 RuntimeError, index에러가 난다. 
    # 이를 물어보니 1,2를 넣었을때 밑에 있는 반복문에서 없는 index에 접근하기 때문이라고 한다.
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    
    for i in range(3,n+1):
        dp[i]=(dp[i-1]+dp[i-2])%10007
        
    return dp[n]

print(build_block(n))