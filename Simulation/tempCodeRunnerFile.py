import sys

def operation_1(matrix):
    return matrix[::-1]
def operation_2(matrix):
    return [row[::-1] for row in matrix]
def operation_3(matrix):
    return [list(row) for row in zip(*matrix[::-1])]
def operation_4(matrix):
    return [list(row) for row in zip(*matrix)][::-1]
def operation_5(matrix):
    n,m=matrix,len(matrix[0])
    new_matrix=[[0]*m for _ in range(n)]
    half_n,half_m=n//2,m//2
    
    for i in range(half_n):
        for j in range(half_m):
            new_matrix[i][j+half_m]=matrix[i][j]
            new_matrix[i+half_n][j+half_m]=matrix[i][j+half_m]
            new_matrix[i+half_n][j]=matrix[i+half_n][j+half_m]
            new_matrix[i][j]=matrix[i+half_n][j]
            
    return new_matrix
def operation_6(matrix):
    n,m=matrix,len(matrix[0])
    new_matrix=[[0]*m for _ in range(n)]
    half_n,half_m=n//2,m//2
    
    for i in range(half_n):
        for j in range(half_m):
            new_matrix[i+half_n][j]=matrix[i][j]
            new_matrix[i+half_n][j+half_m]=matrix[i+half_n][j]
            new_matrix[i][j+half_m]=matrix[i+half_n][j+half_m]
            new_matrix[i][j]=matrix[i][j+half_m]
            
    return new_matrix 
    
    
input = sys.stdin.read
data=input().split()

N,M,R=int(data[0]),int(data[1]),int(data[2])
matrix=[]
idx=3

for i in range(N):
    matrix.append([int(x) for x in data[idx:idx+M]])
    idx+=M
    
operation=[int(x) for x in data[idx]]

for op in operation:
    if op==1:
        matrix=operation_1(matrix)
    elif op==2:
        matrix=operation_2(matrix)
    elif op==3:
        matrix=operation_3(matrix)
    elif op==4:
        matrix=operation_4(matrix)
    elif op==5:
        matrix=operation_5(matrix)
    elif op==6:
        matrix=operation_6(matrix)
        
    for row in matrix:
        print(" ".join(map(str,row)))
        