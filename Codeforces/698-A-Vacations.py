n = int(input())
arr = list(map(int, input().split()))

rest = [float('inf')] * n
contest = [float('inf')] * n
gym = [float('inf')] * n

for i in range(n):
    if i == 0:
        rest[0] = 1
        contest[0] = 0 if arr[0] in [1, 3] else 1
        gym[0] = 0 if arr[0] in [2, 3] else 1
    else:
        rest[i] = min(rest[i-1] + 1, contest[i-1] + 1, gym[i-1] + 1)
        
        if arr[i] in [1, 3]:
            contest[i] = min(rest[i-1], gym[i-1])
        else:
            contest[i] = rest[i]  # No contest today
        
        if arr[i] in [2, 3]:
            gym[i] = min(rest[i-1], contest[i-1])
        else:
            gym[i] = rest[i]  # No gym today

print(min(rest[n-1], contest[n-1], gym[n-1]))
