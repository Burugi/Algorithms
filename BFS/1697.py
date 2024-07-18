from collections import deque

def bfs(start,target):
    if start==target:
        return 0
    
    max_limit=100001
    visited=[False]*max_limit
    queue=deque([(start,0)])
    visited[start]=True
    
    while queue:
        position, time=queue.popleft()
        
        for next_pos in (position-1,position+1,2*position):
            if 0<=next_pos<max_limit and not visited[next_pos]:
                if next_pos==target:
                    return time +1
                queue.append((next_pos,time+1))
                visited[next_pos]=True
    return -1                

n,k=map(int,input().split())
print(bfs(n,k))