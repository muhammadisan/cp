from collections import defaultdict

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    leaf_found, x, y = False, 1, 0
    for leaf in graph:
        if leaf_found:
            break
        if len(leaf) == 1:
            leaf_found = True
            y = len(graph[leaf[0]]) - 1
            mid = graph[leaf[0]]
            for m in mid:
                x = max(x, len(graph[m]))
                
    print(x, y)