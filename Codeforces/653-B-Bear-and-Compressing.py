from collections import defaultdict, deque  

n, q = map(int, input().split())
d = defaultdict(list)
st = set()
for _ in range(q):
    a, b = input().split()
    d[b].append(a)
    st.add(b)
    
dp = [0]*(n+1)
dq = deque(['a'])
while dq:
    current = dq[0]
    if len(current) > n:
        break
        
    dp[len(current)] += 1
    dq.popleft()
    if current[0] in st:
        for val in d[current[0]]:
            dq.append(val + current[1:])
            
print(dp[n])