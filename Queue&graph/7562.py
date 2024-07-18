from collections import deque

def bfs(l, start, end):
    directions = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    queue = deque([start])
    visited = [[False] * l for _ in range(l)]
    visited[start[0]][start[1]] = True
    moves = 0

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if (x, y) == end:
                return moves
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        moves += 1

    return -1

t = int(input())
results = []
for _ in range(t):
    l = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    results.append(bfs(l, start, end))

for result in results:
    print(result)
