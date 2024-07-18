from collections import deque

def bfs(start,target):
    max_limit=100001
    visited=[-1]*max_limit
    queue=deque([start])
    visited[start]=start
    
    while queue:
        position=queue.popleft()
        
        if position==target:
            break
        for next_pos in (position-1,position+1,2*position):
            if 0<=next_pos<max_limit and visited[next_pos]==-1:
                visited[next_pos]=position
                queue.append(next_pos)
                
    path=[]
    pos=target
    while pos!=start: # 여기를 target으로 뒀음
        path.append(pos)
        pos=visited[pos]
    path.append(start)
    
    path.reverse()
    return len(path)-1,path            

n,k=map(int,input().split())
time, path=bfs(n,k)
print(time)
print(' '.join(map(str,path)))