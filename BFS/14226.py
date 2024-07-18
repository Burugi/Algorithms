from collections import deque

def bfs(s):
    max_limit=2001
    visited=[[-1]*max_limit for _ in range(max_limit)]
    queue=deque([(1,0)])
    visited[1][0]=0
    
    while queue:
        screen, clipboard=queue.popleft()
        
        if screen==s:
            return visited[screen][clipboard]
        
        if visited[screen][screen]==-1:
            visited[screen][screen]=visited[screen][clipboard]+1
            queue.append((screen,screen))
        
        if screen+clipboard<max_limit and visited[screen+clipboard][clipboard]==-1:
            visited[screen+clipboard][clipboard]=visited[screen][clipboard]+1
            queue.append((screen+clipboard,clipboard))
            
        if screen-1>0 and visited[screen-1][clipboard]==-1:
            visited[screen-1][clipboard]=visited[screen][clipboard]+1
            queue.append((screen-1,clipboard))
    return -1
            
s= int(input())
print(bfs(s))