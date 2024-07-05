from itertools import permutations
n = int(input().strip())
arr = list(map(int,input().strip().split()))

def get_sum(arr):
    total_sum=0
    for i in range(len(arr)-1):
        total_sum+=abs(arr[i]-arr[i+1])
        
    return total_sum

def solve(arr):
    possible_per=permutations(arr)
    max_value=float("-inf")
    for per in possible_per:
        max_value=max(get_sum(per),max_value)
    
    print(max_value)
    
solve(arr)