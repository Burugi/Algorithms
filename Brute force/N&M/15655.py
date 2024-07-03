import sys
input = sys.stdin.read

def backtracking(n,m,depth,start,data,path,used,results):
    if depth==m:
        results.append(path[:])
        return
    # 시작점이 되는 부분을 start로 진행하는 것 
    for i in range(start,n):
        if not used[i]:
            used[i]=True
            path.append(data[i])
            backtracking(n,m,depth+1,i,data,path,used,results)
            path.pop()
            used[i]=False
            
def solve(n,m,data):
    results=[]
    used=[False] *n
    backtracking(n,m,0,0,data,[],used,results)
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
