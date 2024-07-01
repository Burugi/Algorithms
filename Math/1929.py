import sys
import math

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False # 0과 1은 소수가 아님

    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    return is_prime

# 내어쓰기는 shift+tab이다. 
input = sys.stdin.read
data = input().split()
M = int(data[0])
N = int(data[1])

is_prime = sieve_of_eratosthenes(N)

for i in range(M, N + 1):
    if is_prime[i]:
        print(i)