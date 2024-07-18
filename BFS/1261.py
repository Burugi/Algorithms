import heapq

def dijkstra(n, m, maze):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dist = [[float('inf')] * m for _ in range(n)]
    dist[0][0] = 0
    pq = [(0, 0, 0)]  # (부순 벽의 수, x, y)

    while pq:
        broken, x, y = heapq.heappop(pq)
        
        if x == n - 1 and y == m - 1:
            return broken
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                new_broken = broken + maze[nx][ny]
                if new_broken < dist[nx][ny]:
                    dist[nx][ny] = new_broken
                    heapq.heappush(pq, (new_broken, nx, ny))
    return -1

m, n = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

print(dijkstra(n, m, maze))
