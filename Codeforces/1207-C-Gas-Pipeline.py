t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    s = input()
    
    high = [float('inf')]*(n + 1)
    low = [float('inf')]*(n + 1)
    
    low[0] = b
        
    for i in range(n):
        if s[i] == '0':
            high[i+1] = min(high[i] + a + 2*b, low[i] + 2*a + 2*b)
            low[i+1] = min(high[i] + 2*a + b, low[i] + a + b)
        else:
            high[i+1] = high[i] + a + 2*b
    
    print(low[n])