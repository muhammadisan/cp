def dfs(node, search, graph):
    visited[node] = True
    
    if node == search:
        return True
        
    for a in graph[node]:
        if not visited[a]:
            if dfs(a, search, graph):
                return True
                
    return False
    
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
count = [0]*(n+1)
for _ in range((n*(n-1))//2-1):
    x, y = map(int, input().split())
    count[x] += 1
    count[y] += 1
    graph[x].append(y)
    
a, b = 0, 0
for i in range(1,n+1):
    if count[i] != n-1:
        if a == 0:
            a = i
        else:
            b = i
            
if dfs(a, b, graph):
    print(a, b)
else:
    print(b, a)