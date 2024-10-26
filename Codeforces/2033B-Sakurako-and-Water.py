t = int(input())
for _ in range(t):
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    
    ans = 0
    for j in range(n-1, -1, -1):
        min_upper = float('inf')
        min_bottom = float('inf')
        for i in range(n-j):
            min_upper = min(min_upper, grid[i][i+j])
            min_bottom = min(min_bottom, grid[i+j][i])
            
        if min_upper < 0:
            ans -= min_upper
        if min_bottom < 0 and j != 0:
            ans -= min_bottom
    
    print(ans)