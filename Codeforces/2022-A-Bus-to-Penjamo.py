t = int(input())
for _ in range(t):
    n, r = map(int, input().split())
    a = list(map(int, input().split()))
    
    ans = 0
    odd = 0
    seats = 2*r
    for i in range(n):
        if a[i] % 2 == 0:
            ans += a[i]
            seats -= a[i]
        else:
            ans += a[i]-1
            odd += 1
            seats -= a[i]-1
    if odd <= seats/2:
        ans += odd
    else:
        seats //= 2
        ans += seats
        odd -= seats
        ans -= odd
    print(ans)
