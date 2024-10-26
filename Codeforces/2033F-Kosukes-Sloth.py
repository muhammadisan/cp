MOD = 10**9 + 7
 
def pisano(k):
    prev, curr = 1, 1
    for i in range(0, k * k):
        prev, curr = curr, (prev + curr) % k
        if prev == 1 and curr == 1:
            return i + 1
 
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    
    if k == 1:
        print(n % MOD)
        continue
        
    idx = []
    prev, curr = 1, 1
    for i in range(3, pisano(k)+1):
        prev, curr = curr, (prev + curr) % k
        if curr == 0:
            idx.append(i)
             
    idx_len = len(idx)
    ans = idx[-1] * (n // idx_len) % MOD
    if n % idx_len != 0:
        ans += idx[n % idx_len - 1]
        ans %= MOD
    print(ans)