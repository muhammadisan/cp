t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # 0 <= x < k is on and k <= x < 2k is off
    # All light will turned on at least in max_a minute
    max_a = max(a)
    mod_diff = [(max_a - ai) % (2 * k) for ai in a]
    
    # Adjust mod_diff to ensure values between -k and k
    # Everything in negative are currently turned off
    mod_adjusted = [x - 2 * k if x > k else x for x in mod_diff]
    
    max_mod = max(mod_adjusted)
    min_mod = min(mod_adjusted)
    
    # Check if the range between max_mod and min_mod exceeds k
    # We will increase all light by abs(min_mod) to make all light turned on
    if max_mod - min_mod >= k:
        print(-1)
    else:
        print(max_a - min_mod)
