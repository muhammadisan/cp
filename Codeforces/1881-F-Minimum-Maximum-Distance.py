from collections import deque
import math

def bfs(start, graph, marked):
    visited = [False] * len(graph)
    q = deque([start])
    farthest_node = start
    while q:
        node = q.popleft()
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                q.append(neighbor)
                if marked[neighbor]:
                    farthest_node = neighbor
    return farthest_node

def bfs_distances(start, graph):
    visited = [False] * len(graph)
    distances = [0] * len(graph)
    q = deque([start])
    visited[start] = True
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
                distances[neighbor] = distances[node] + 1
    return distances

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    if k == 1:
      print(0)
      continue
    
    # marked node
    marked = [False] * (n + 1)
    for mark in a:
        marked[mark] = True
        
    # Find farthest marked node from a[0]
    v2 = bfs(a[0], graph, marked)
    # Find farthest marked node from v2
    v3 = bfs(v2, graph, marked)
    
    # Calculate distances from v2 to all nodes
    distance2 = bfs_distances(v2, graph)
    
    # ans = ceil(distance(v2 to  v3)/2)
    print(math.ceil(distance2[v3]/2))
