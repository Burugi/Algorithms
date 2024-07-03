# 15649에서 순서를 가지게 된 것이다. 
import sys
input = sys.stdin.read

# 순서를 가지게 되면서 뒤의 내용을 신경쓸 필요가 없어짐
# start만 가지고 있으면 된다. 
def backtracking(n,m,start,path,results):
    if len(path)==m:
        results.append(path[:])
        return
    for i in range(start,n+1):
        path.append(i)
        # i보다 1큰 수를 시작으로 해서 다시 찾아나가는 것
        backtracking(n,m,i+1,path,results)
        path.pop()
            
def solve(n,m):
    results=[]
    backtracking(n,m,1,[],results)
    for result in results:
        print(' '.join(map(str,result)))
    

input_data = input().strip().split()
n, m = int(input_data[0]),int(input_data[1])

solve(n,m)
