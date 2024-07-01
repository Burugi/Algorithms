def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b, gcd_value):
    return a * b // gcd_value

# 입력 받기
a, b = map(int, input().split())

# 최대공약수 구하기
gcd_value = gcd(a, b)

# 최소공배수 구하기
lcm_value = lcm(a, b, gcd_value)

# 결과 출력
print(gcd_value)
print(lcm_value)
