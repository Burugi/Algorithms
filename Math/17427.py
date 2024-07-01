'''
n^2까지는 될 것 같다.
'''
# def sumOfNum(a):
#     sum=0
#     for i in range(1,a+1):
#         if a%i==0:
#             sum+=i
            
#     return sum

# num = input()
# total_sum=0
# for i in range(int(num)):
#     total_sum+=sumOfNum(i+1)
# print(total_sum)
# -> O^2라서 시간초과

def sum_of_divisors(n):
    total_sum = 0
    # 각 수 i에 대해 i의 배수들에 i를 더해줍니다.
    for i in range(1, n + 1):
        total_sum += i * (n // i)
    return total_sum

# 입력 받기
n = int(input().strip())

# 결과 출력
print(sum_of_divisors(n))
'''
1의 배수가 n일때 총 n개 있으므로 n*1
2의 배수가 n일때 총 n//2개 있으므로 n//2 * 2
쉽게 말하면 가로로 묶으면 O^2인 문제를 세로로 표현하면 O가 된다.
'''