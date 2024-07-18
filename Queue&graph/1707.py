import sys
from collections import deque

input =sys.stdin.read

def bfs(graph,start,colors):
    queue=deque([start])
    colors[start]=1 
    
    while queue:
        node=queue.popleft()
        current_color=colors[node]
        next_color= 2 if current_color==1 else 1
        
        for neighbor in graph[node]:
            if colors[neighbor]==0:
                colors[neighbor]=next_color
                queue.append(neighbor)
            elif colors[neighbor]==current_color:
                return False
    return True

def is_bipartite(graph,n):
    colors=[0]*(n+1)
    
    for i in range(1,n+1):
        if colors[i]==0:
            if not bfs(graph,i,colors):
                return False
    return True

data = input().strip().split()
index = 0
k = int(data[index])
index += 1

results = []

for _ in range(k):
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        graph[u].append(v)
        graph[v].append(u)
        
    if is_bipartite(graph,n):
        results.append("YES")
    else:
        results.append("NO")
        
for result in results:
    print(result)