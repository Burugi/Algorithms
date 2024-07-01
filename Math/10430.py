A, B, C=map(int,input().split())
# 여러 값을 입력받는 방법 map을 사용 
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)