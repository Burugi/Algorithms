N = int(input())
board = [list(input().strip()) for _ in range(N)]
# 여러줄을 한꺼번에 입력받는 방법 
max_candy=0

def check_max_candy(borad,N):
    max_candy=1
    for i in range(N):
        count =1 
        for j in range(1,N):
            if board[i][j]==board[i][j-1]:
                count+=1
            else:
                count=1
            max_candy=max(max_candy,count)
    for j in range(N):
        count =1 
        for i in range(1,N):
            if board[i][j]==board[i-1][j]:
                count+=1
            else:
                count=1
            max_candy=max(max_candy,count)
    return max_candy

for i in range(N):
    for j in range(N):
        if j+1 < N :
            board[i][j],board[i][j+1]=board[i][j+1],board[i][j]
            max_candy=max(max_candy,check_max_candy(board,N))
            board[i][j],board[i][j+1]=board[i][j+1],board[i][j]
        if i+1<N:
            board[i][j],board[i+1][j]=board[i+1][j],board[i][j]
            max_candy=max(max_candy,check_max_candy(board,N))
            board[i][j],board[i+1][j]=board[i+1][j],board[i][j]
            
print(max_candy)


def check_max_candy(board, N):
    max_candy = 1
    for i in range(N):
        count = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                count += 1
            else:
                count = 1
            max_candy = max(max_candy, count)
    
    for j in range(N):
        count = 1
        for i in range(1, N):
            if board[i][j] == board[i-1][j]:
                count += 1
            else:
                count = 1
            max_candy = max(max_candy, count)
    
    return max_candy
