from itertools import permutations

n=int(input().strip())

arr=range(1,n+1)

for permutation in permutations(arr):
    print(' '.join(map(str,permutation)))