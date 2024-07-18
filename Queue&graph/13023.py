import sys
input = sys.stdin.read

def dfs(graph,visited,node,depth):
    if depth == 4 :
        return True
    visited[node]=True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(graph,visited,neighbor,depth+1): # neighbor을 node라고 했네
                return True
    visited[node]=False
    return False

data=input().strip().split()
n=int(data[0])
m=int(data[1])

graph=[[] for _ in range(n)]
index=2

for _ in range(m):
    a=int(data[index])
    b=int(data[index+1])
    graph[a].append(b)
    graph[b].append(a)
    index+=2

found=False

for i in range(n):
    visited=[False]*n
    if dfs(graph,visited,i,0):
        found=True
        break
    
print(1 if found else 0)