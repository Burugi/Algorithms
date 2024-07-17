import sys
input =sys.stdin.read

def consecutive_sum(n,a):
    max_current = max_global = a[0]
    
    for num in a[1:]:
        max_current=max(num,num+max_current)
        if max_current>max_global:
            max_global=max_current
    
    return max_global

data=input().strip().split()
N=int(data[0])
A=list(map(int,data[1:]))

print(consecutive_sum(N,A))