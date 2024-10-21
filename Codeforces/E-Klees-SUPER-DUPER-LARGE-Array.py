def ternary_search(n, k):
    l = 0
    r = n-1
    while r - l > 2:
        m1 = l + (r - l) // 3
        m2 = r - (r - l) // 3
        
        if f(m1, n, k) > f(m2, n, k):
            l = m1
        else:
            r = m2
    
    best = l
    for i in range(l, r + 1):
        if f(i, n, k) < f(best, n, k):
            best = i
    return f(best, n, k)

def f(x, n, k):
    return abs(n*k + n*(n-1)//2 - 2*x*k - x*(x-1))
    

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(ternary_search(n, k))
    