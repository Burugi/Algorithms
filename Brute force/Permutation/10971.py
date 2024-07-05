import sys
from itertools import permutations
input =sys.stdin.read

input_data=input().strip().split()
n=int(input_data[0])
index=1
board=[]
for _ in range(n):
    board.append(list(map(int,input_data[index:index+n])))
    index+=n

def get_cost(per,board):
    total_cost=0
    n=len(per)
    
    for i in range(n-1):
        cost=board[per[i]][per[i+1]]
        if cost==0:
            return float("inf")
        total_cost+=cost
    
    cost=board[per[-1]][per[0]]
    if cost==0:
        return float("inf")
    total_cost+=cost
    
    return total_cost

def solve(n,board):
    arr=range(n)
    possible_per=permutations(arr)
    min_value=float("inf")
    for per in possible_per:
        min_value=min(min_value,get_cost(per,board))
    
    print(min_value)
    
solve(n,board)