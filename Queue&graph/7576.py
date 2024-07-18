from collections import deque

def bfs(tomato_farm,n,m):
    direction=[(-1,0),(1,0),(0,1),(0,-1)]
    queue=deque()
    
    for i in range(n):
        for j in range(m):
            if tomato_farm[i][j]==1:
                queue.append((i,j))
                
    while queue:
        x,y=queue.popleft()
        for dx,dy in direction:
            nx,ny=x+dx,y+dy
            if 0 <= nx < n and 0 <= ny < m and tomato_farm[nx][ny]==0:
                tomato_farm[nx][ny]=tomato_farm[x][y]+1
                queue.append((nx,ny))   
                
    max_days=0
    for row in tomato_farm:
        for value in row:
            if value==0:
                return -1
            max_days=max(max_days,value)
    return max_days-1

n, m = map(int,input().split())
tomato_farm=[list(map(int,input().split())) for _ in range(m)] 

print(bfs(tomato_farm,m,n)) # 행과 열의 일반적인 순서와 반대임