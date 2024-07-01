# ctrl+shift+r : 리팩토링
def findNum(a):
    i=1
    num=1
    while True:
       if num%a==0:
           print(i)
           break
       num+=pow(10,i)
       #  num=num*10+1 -> 이게 더 좋아보임, 뒤로 1을 붙이냐, 앞으로 1을 붙이냐의 차이인데
       i+=1

import sys
input = sys.stdin.read
# 줄바꿈 입력을 받을 때는 이렇게 받아야하는구나 
inputs = input().strip().split()

# 각 입력 값에 대해 find_num 함수 호출
for value in inputs:
    n = int(value)
    if n % 2 != 0 and n % 5 != 0:
        findNum(n)
