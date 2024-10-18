mod = 1000000007

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    P = a[0]*a[1]
    pref = a[0] + a[1]
    for i in range(2, n):
        P += pref*a[i]
        P %= mod
        pref += a[i]
        pref %= mod
    Q = (n*(n-1))//2
    
    ans = (P * pow(Q, mod-2, mod)) % mod
    print(ans)