import sys
input=sys.stdin.read

input_data=input().strip().split()
n,m,k=int(input_data[0]),int(input_data[1]),int(input_data[2])
board=[]
index=3
for i in range(n):
    board.append(list(map(int,input_data[index:index+m])))
    index+=m

def backtracking(n,m,k,board,start,path,visited,results):
    if len(path)==k:
        results.append(sum(path))
        return 
    
    for i in range(start,n*m):
        row=i//m
        col=i%m
        
        if visited[row][col]:
            continue
        
        if (row>0 and visited[row-1][col] or
            row<n-1 and visited[row+1][col] or
            col>0 and visited[row][col-1] or
            col<m-1 and visited[row][col+1]
            ):
            continue
        
        visited[row][col]=True
        path.append(board[row][col])
        backtracking(n,m,k,board,i+1,path,visited,results)
        path.pop()
        visited[row][col]=False
    
def solve(n,m,k,board):
    results=[]
    visited=[[False]*m for _ in range(n)]
    backtracking(n,m,k,board,0,[],visited,results)
    print(max(results))
    

solve(n,m,k,board)

