

import sys
input = sys.stdin.read
# 내가 수정해서 맞췄다 탈출 조건이 count로만 가정하면 되는 문제였다.

def backtracking(n,m,count,path,data,results):
    if count==m:
        results.append(path[:])
        return
    
    for i in range(n):
        path.append(data[i])
        # start를 i부터 시작하는 거면 된다.
        backtracking(n,m,count+1,path,data,results)
        path.pop()
            
def solve(n,m,data):
    results=[]
    backtracking(n,m,0,[],data,results)
    for result in results:
        print(' '.join(map(str,result)))
    

input_data = input().strip().split()
n, m = int(input_data[0]),int(input_data[1])

data=[]
index=2

for i in range(n):
    data.append(int(input_data[index+i]))
data.sort()

solve(n,m,data)
