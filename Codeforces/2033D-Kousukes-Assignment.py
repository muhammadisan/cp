t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    prefsum = [0]*(n + 1)
    prefsum[1] = a[0]
    for i in range(2, n + 1):
        prefsum[i] = prefsum[i-1] + a[i-1]
        
    ans = 0
    s = set()
    i = 0
    while i < n + 1:
        if prefsum[i] in s:
            ans += 1
            s = set()
            s.add(prefsum[i])
        else:
            s.add(prefsum[i])
        i += 1
        
    print(ans)