n, a, b, c = map(int, input().split())
dp = [0]*(n + 1)

for idx in [a, b, c]:
    if idx <= n:
        dp[idx] = 1

for i in range(min(a, b, c), n + 1):
    for idx in [a, b, c]:
        if i >= idx and dp[i - idx] != 0:
            dp[i] = max(dp[i], dp[i - idx] + 1)

print(dp[n])
