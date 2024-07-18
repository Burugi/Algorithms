import sys
sys.setrecursionlimit(10000)
input=sys.stdin.read

def dfs(graph,v,visited):
    visited[v]=True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph,neighbor,visited)

data=input().strip().split()
n=int(data[0])
m=int(data[1])

graph=[[] for _ in range(n+1)]
index=2

for _ in range(m):
    a=int(data[index])
    b=int(data[index+1])
    graph[a].append(b)
    graph[b].append(a)
    index+=2

visited = [False] * (n + 1)
count = 0

for i in range(1,n+1):
    if not visited[i]:
        dfs(graph,i,visited)
        count+=1

print(count)