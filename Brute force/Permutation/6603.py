import sys
from itertools import combinations

input = sys.stdin.read

def solve():
    input_data = input().strip().split("\n")
    results = []
    
    for line in input_data:
        if line == "0":
            break
        nums = list(map(int, line.split()))
        k = nums[0]
        s = nums[1:]
        
        comb = combinations(s, 6)
        for c in comb:
            results.append(" ".join(map(str, c)))
        results.append("")
    
    print("\n".join(results).strip())

solve()
