t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    s = input()
    
    dp = [0] * n
    visited = [False] * n
    
    for i in range(n):
        if visited[i]:
            continue
        
        # Initialize the list to track nodes in the current cycle
        cycle = []
        current = i
        black_count = 0
        
        # Traverse the cycle and mark nodes visited
        while not visited[current]:
            visited[current] = True
            cycle.append(current)
            if s[current] == '0':
                black_count += 1
            current = p[current] - 1  # Convert to zero-based index
        
        # Assign the black count to all nodes in the cycle
        for node in cycle:
            dp[node] = black_count
    
    print(*dp)
