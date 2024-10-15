import math

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    max_a = 0
    sum_a = 0
    for el in a:
        max_a = max(max_a, el)
        sum_a += el
    ans = max(max_a, math.ceil(sum_a/x))
    print(ans)