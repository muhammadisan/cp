N, W = map(int, input().split())
w, v = [], []
total_value = 0
for i in range(N):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)
    total_value += b
    
dp = [float('inf')]*(total_value + 1)
dp[0] = 0  # 0 value for 0 weight

# find minimum weight required for target value
for i in range(N):
    for value in reversed(range(v[i], total_value + 1)):
        dp[value] = min(dp[value], dp[value - v[i]] + w[i])
        
max_value = 0
# find max value
for value in range(total_value + 1):
    if dp[value] <= W:
        max_value = max(max_value, value)

print(max_value)