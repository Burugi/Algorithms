import sys
input=sys.stdin.read

def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=n:
        return 0
    if grid[x][y]==0:
        return 0
    
    grid[x][y]=0
    count=1
    count+= dfs(x-1,y)
    count+= dfs(x+1,y)
    count+= dfs(x,y-1)
    count+= dfs(x,y+1)
    return count

data=input().strip().split()
n=int(data[0])
grid=[]
index=1
for i in range(n):
    grid.append([int(x) for x in data[index]])
    index+=1
    
result=[]
for i in range(n):
    for j in range(n):
        if grid[i][j]==1:
            result.append(dfs(i,j))

result.sort()
print(len(result))
for count in result:
    print(count)