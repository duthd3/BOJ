n = int(input())

for i in range(0, n):
    k = int(input())
    # dp[1] = 1
    # dp[2] = 2
    # dp[3] = 4
    # dp[4] = 7
    # dp[5] = 13
    # dp[6] = 24
    # dp[i] = dp[i-1] + dp[i-2] + dp[i-3] (i>=4)
    dp = [0] * (k+1)
    for j in range(1, k + 1):
        if j == 1:
            dp[j] = 1
        elif j == 2:
            dp[j] = 2
        elif j == 3:
            dp[j] = 4
        else:
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
    print(dp[j])
