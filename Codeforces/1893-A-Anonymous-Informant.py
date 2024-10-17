t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    
    curr_val = b[n-1]
    curr_idx = n-1
    
    ans = "Yes"
    iterate = min(k, n)
    while iterate > 0:
        if curr_val > n:
            ans = "No"
            break
            
        curr_idx = ((curr_idx - curr_val) % n + n) % n
        curr_val = b[curr_idx]
        
        iterate -= 1
            
    print(ans)