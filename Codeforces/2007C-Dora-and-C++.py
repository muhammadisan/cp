from math import gcd

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    c = list(map(int, input().split()))
    
    _gcd = gcd(a, b)
    
    if n == 1 or _gcd == 1:
        print(0)
        continue
        
    c = sorted([el % _gcd for el in c])
    ans = c[n-1] - c[0]
    for i in range(len(c)-1):
        ans = min(ans, c[i] + _gcd - c[i+1])
    print(ans)