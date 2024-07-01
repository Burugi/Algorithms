import sys
import math

input = sys.stdin.read

def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False # 0과 1은 소수가 아님

    for i in range(2, int(math.sqrt(max_num)) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
    
    return is_prime

MAX = 1000000
is_prime = sieve_of_eratosthenes(MAX)

data = input().strip().split()
numbers = list(map(int, data))

for n in numbers:
    if n == 0:
        break
    found = False
    for i in range(3, n // 2 + 1):
        if is_prime[i] and is_prime[n - i]:
            print(f"{n} = {i} + {n - i}")
            found = True
            break
    if not found:
        print("Goldbach's conjecture is wrong.")
