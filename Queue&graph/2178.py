from collections import deque

def dfs(maze,n,m):
    direction=[(-1,0),(1,0),(0,1),(0,-1)]
    queue=deque([(0,0)])
    while queue:
        x,y=queue.popleft()
        for dx,dy in direction:
            nx,ny=x+dx,y+dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny]==1:
                queue.append((nx,ny))
                maze[nx][ny]=maze[x][y]+1
    return maze[n-1][m-1]

n, m = map(int,input().split())
maze=[list(map(int,input().strip())) for _ in range(n)] # split으로 썼었다

print(dfs(maze,n,m))