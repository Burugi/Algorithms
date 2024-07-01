# import sys
# inputs=sys.stdin.read().split()
# # ctrl+z로 입력을 그만두는 것이 가능

# def findNum(a):
#     sum = 0
#     for i in range(1,a+1):
#         sum+=i*(a//i)
#     return sum

# for i in range(int(inputs[0])):
#     total_sum=0
#     total_sum+=findNum(int(inputs[i+1]))
#     print(total_sum)
# # 17427문제를 그대로 쓴다면 시간초과... 

# 최대값 설정
MAX=1000000

# DP 1로 초기화
dp = [1]*(MAX+1)

# S: 값 누적 리스트
s = [0]*(MAX+1)

for i in range(2, MAX+1):
    j=1
    while i*j <= MAX:
    	# i의 배수에 값 추가
        dp[i*j] += i
        j += 1
# 아 그러니까 쭉 더해나가는 거구나 이건 마치 체와 같이 더하는 것과 같구나 

for i in range(1, MAX+1):
	# 누적 값 계산
    s[i] = s[i-1] + dp[i]

n = int(input())
ans=[]
for _ in range(n):
    a=int(input())
    ans.append(s[a])
print('\n'.join(map(str, ans))+'\n')
# python 3로 하면 시간초과 에러가 뜨는데 Pypy3로 해야함
