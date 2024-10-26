def isNotBorder(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

neighbor = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def dfs(x, y, n, m, grid, visited):
    stack = [(x, y)]
    visited[x][y] = True
    count = 1

    while stack:
        cx, cy = stack.pop()
        for i, j in neighbor:
            nx, ny = cx + i, cy + j
            if isNotBorder(nx, ny, n, m) and not visited[nx][ny] and grid[nx][ny] == '.':
                visited[nx][ny] = True
                count += 1
                stack.append((nx, ny))
    return count

def lake_to_land(x, y, n, m, grid, visited):
    stack = [(x, y)]
    visited[x][y] = True
    grid[x][y] = "*"

    while stack:
        cx, cy = stack.pop()
        for i, j in neighbor:
            nx, ny = cx + i, cy + j
            if isNotBorder(nx, ny, n, m) and not visited[nx][ny] and grid[nx][ny] == '.':
                visited[nx][ny] = True
                grid[nx][ny] = "*"
                stack.append((nx, ny))

n, m, k = map(int, input().split())
grid = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# Kunjungi semua 'laut' di batas grid
for i in [0, n - 1]:
    for j in range(m):
        if grid[i][j] == '.' and not visited[i][j]:
            dfs(i, j, n, m, grid, visited)
for i in range(n):
    for j in [0, m - 1]:
        if grid[i][j] == '.' and not visited[i][j]:
            dfs(i, j, n, m, grid, visited)

# Cari semua danau yang terkurung di dalam grid
lakes_size = []
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if grid[i][j] == '.' and not visited[i][j]:
            count = dfs(i, j, n, m, grid, visited)
            lakes_size.append((count, i, j))

# Urutkan danau berdasarkan ukuran dan hitung sel yang akan diubah
lakes_size.sort()
visited = [[False] * m for _ in range(n)]
count_cells = 0

for count, x, y in lakes_size[:len(lakes_size) - k]:
    count_cells += count
    lake_to_land(x, y, n, m, grid, visited)

print(count_cells)
for g in grid:
    print("".join(g))
