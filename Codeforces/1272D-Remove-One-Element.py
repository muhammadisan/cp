n = int(input())
a = list(map(int, input().split()))

# dp1[i] -> length of increasing subarray ending at index i
# dp2[i] -> length of increasing subarray starting at index i
dp1 = [1] * n
dp2 = [1] * n

# Calculate dp1: longest increasing subarray ending at each position
for i in range(1, n):
    if a[i] > a[i - 1]:
        dp1[i] = dp1[i - 1] + 1

# Calculate dp2: longest increasing subarray starting at each position
for i in range(n - 2, -1, -1):
    if a[i] < a[i + 1]:
        dp2[i] = dp2[i + 1] + 1

# Find the maximum possible subarray length after removing at most one element
ans = max(dp1)  # Without removing any element

for i in range(1, n - 1):
    if a[i - 1] < a[i + 1]:  # Can remove a[i] and merge two increasing subarrays
        ans = max(ans, dp1[i - 1] + dp2[i + 1])

print(ans)
