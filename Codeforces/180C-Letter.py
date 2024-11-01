s = input()
n = len(s)

# Initialize the dp arrays
up = [float('inf')] * (n + 1)
low = [float('inf')] * (n + 1)

# Initial cases for first character
up[0] = 0
low[0] = 0
up[1] = 0 if s[0].isupper() else 1
low[1] = 0 if s[0].islower() else 1

# Fill the dp arrays
for i in range(1, n):
    if s[i].isupper():
        up[i+1] = up[i]
        low[i+1] = min(up[i] + 1, low[i] + 1)
    else:
        up[i+1] = up[i] + 1
        low[i+1] = min(up[i], low[i])

# Output the minimum number of changes
print(min(up[n], low[n]))
