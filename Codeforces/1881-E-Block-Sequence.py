t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [float('inf')]*(n+1)
    dp[n] = 0
    dp[n-1] = 1
    for i in reversed(range(n-1)):
        take = float('inf')
        if i+a[i] < n:
            take = dp[i+a[i]+1]
        not_take = 1 + dp[i+1]
        dp[i] = min(take, not_take)
            
    print(dp[0])