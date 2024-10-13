t = int(input())
for _ in range(t):
    k, n = map(int, input().split())
    half_left = (k+1)//2
    half_right = k - half_left
    idx = 1
    power_two = 1
    
    while n >= half_left + idx:
        if n < half_left + idx:
            break
        idx += half_left
        split_part = half_right
        half_left = (split_part+1)//2
        half_right = split_part - half_left
        power_two *= 2
        
    result = power_two * (2*(n-idx)+1)
    print(result)