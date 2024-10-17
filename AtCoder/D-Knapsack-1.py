N, W = map(int, input().split())
w, v = [], []
for i in range(N):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]  # Tambah dimensi untuk item ke-0

for i in range(1, N+1):
    for j in range(W+1):
        dp[i][j] = dp[i-1][j]  # Tidak mengambil barang i-1
        if j >= w[i-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-w[i-1]] + v[i-1])  # Mengambil barang i-1

print(dp[N][W])
