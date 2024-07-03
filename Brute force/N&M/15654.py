import sys
input = sys.stdin.read
# 자신이 사용했다는 것을 확인하기 위한 used 변수가 필요한 문제다
# 무엇이 필요한지 확실하게 알아야한다.

def backtracking(n,m,depth,data,path,used,results):
    if depth==m:
        results.append(path[:])
        return
    
    for i in range(n):
        if not used[i]:
            used[i]=True
            path.append(data[i])
            backtracking(n,m,depth+1,data,path,used,results)
            path.pop()
            used[i]=False
            
def solve(n,m,data):
    results=[]
    used=[False] *n
    backtracking(n,m,0,data,[],used,results)
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



# import sys
# input = sys.stdin.read
# # 내가 수정해서 맞췄다 탈출 조건이 count로만 가정하면 되는 문제였다.

# def backtracking(n,m,count,path,data,results):
#     if count==m:
#         results.append(path[:])
#         return
    
#     for i in range(n):
#         path.append(data[i])
#         # start를 i부터 시작하는 거면 된다.
#         backtracking(n,m,count+1,path,data,results)
#         path.pop()
            
# def solve(n,m,data):
#     results=[]
#     backtracking(n,m,0,[],data,results)
#     for result in results:
#         print(' '.join(map(str,result)))
    

# input_data = input().strip().split()
# n, m = int(input_data[0]),int(input_data[1])

# data=[]
# index=2

# for i in range(n):
#     data.append(int(input_data[index+i]))
# data.sort()

# solve(n,m,data)
