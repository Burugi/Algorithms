from collections import deque

def bfs(start, target):
    max_limit = 100001
    visited = [-1] * max_limit
    deque_queue = deque([start])
    visited[start] = 0
    
    while deque_queue:
        current = deque_queue.popleft()
        
        if current == target:
            return visited[current]
        
        for next_pos in (current * 2, current - 1, current + 1): # next_pos의 순서가 중요하다
            # 반례 4 6 -> 2인지 1인지에 대한 내용, 작은 값을 먼저 처리해야할 것이다.
            if 0 <= next_pos < max_limit:
                if next_pos == current * 2 and visited[next_pos] == -1:
                    visited[next_pos] = visited[current]
                    deque_queue.appendleft(next_pos)
                elif (next_pos == current + 1 or next_pos == current - 1) and visited[next_pos] == -1:
                    visited[next_pos] = visited[current] + 1
                    deque_queue.append(next_pos)

n, k = map(int, input().split())
print(bfs(n, k))
