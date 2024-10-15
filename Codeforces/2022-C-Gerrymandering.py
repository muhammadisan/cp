def voteA(s):
    return s.count('A') >= 2

t = int(input())
for _ in range(t):
    n = int(input())
    s0 = 'J' + input()
    s1 = 'J' + input()
    
    dp = [[0] * 3 for _ in range(n + 1)]
    
    dp[1][1] = voteA(s0[1] + s1[1] + s1[2])
    dp[1][2] = voteA(s0[1] + s0[2] + s1[1])
    
    for i in range(3, n + 1):
        # Districts formed by previous three columns
        dp[i][0] = max(
            voteA(s0[i-2:i+1]) + voteA(s1[i-2:i+1]) + dp[i-3][0],
            voteA(s0[i-1] + s0[i] + s1[i]) + dp[i-2][1],
            voteA(s0[i] + s1[i-1] + s1[i]) + dp[i-2][2]
        )
        
        if i <= n - 2:
            dp[i][1] = max(
                voteA(s0[i] + s1[i] + s1[i+1]) + dp[i-1][0],
                voteA(s0[i-2:i+1]) + voteA(s1[i-1:i+2]) + dp[i-3][1]
            )
            dp[i][2] = max(
                voteA(s0[i] + s0[i+1] + s1[i]) + dp[i-1][0],
                voteA(s0[i-1:i+2]) + voteA(s1[i-2:i+1]) + dp[i-3][2]
            )
    
    print(dp[n][0])
