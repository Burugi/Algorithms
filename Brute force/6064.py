import sys
input = sys.stdin.read

input_data= input().strip().split()
# tab으로넘어가는 거 tabout extension으로 가능하다.
T = int(input_data[0])
index = 1
results=[]

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def find_year(M,N,x,y):
    lcm_year = lcm(M,N)
    k=x
    # gcd, lcm을 이용해서 푸는 문제 
    while k<=lcm_year:
        if (k-1)%N +1==y:
            return k
        k+=M
    return -1

for _ in range(T):
    M = int(input_data[index])
    N = int(input_data[index+1])
    x = int(input_data[index+2])
    y = int(input_data[index+3])
    results.append(find_year(M,N,x,y))
    index+=4
    
for result in results:
    print(result)