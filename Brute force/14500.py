import sys

input = sys.stdin.read
# 여러줄을 받을 때는 이런식으로 하기 
# 실제 구현을 이렇게 하는 것을 확인할 수 있었다.
tetrominoes=[
    # I 모양
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(1,0),(2,0),(3,0)],
    # O 모양
    [(0,0),(1,0),(1,1),(0,1)],
    # T 모양
    [(0,0),(0,1),(0,2),(1,1)],
    [(0,1),(1,0),(1,1),(2,1)],
    [(1,0),(0,1),(1,1),(1,2)],
    [(0,0),(1,0),(2,0),(1,1)],
    # L모양
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 1), (1, 1), (2, 1), (2, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (1, 0), (2, 0), (0, 1)],
    [(0, 1), (1, 1), (2, 1), (0, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(1, 0), (1, 1), (1, 2), (0, 0)],
    # S모양
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 1), (1, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (0, 1), (0, 2)]
]

input_data = input().strip().split()
n, m = int(input_data[0]),int(input_data[1])
borad=[]
index=2
for _ in range(n):
    borad.append(list(map(int,input_data[index:index+m])))
    index+=m

def get_max_tetromino_sum(board,n,m):
    total_sum=0
    
    for i in range(n):
        for j in range(m):
            for ter in tetrominoes:
                try:
                    sum_value=sum(board[i+x][j+y] for x,y in ter)
                    total_sum=max(sum_value,total_sum)
                except IndexError:
                    continue
    # index 에러를 다음과 같은 방법으로 해결한 것, 에러 나는 거를 넘어가도록 설계한 게 좋았다. 
    return total_sum

result=get_max_tetromino_sum(borad,n,m)
print(result)