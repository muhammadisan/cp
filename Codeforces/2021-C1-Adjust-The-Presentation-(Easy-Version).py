t = int(input())
for _ in range(t):
    n, m, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    s = set()
    ans = "YA"
    i = 0
    for presenter in b:
        if presenter == a[i]:
            s.add(a[i])
            if i+1 < len(a):
                i += 1
            continue
        elif presenter in s:
            continue
        else:
            ans = "TIDAK"
            break
        
    print(ans)