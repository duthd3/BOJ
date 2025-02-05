t = int(input())

for _ in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    for i in range(2): # 0,1의 dp테이블 채우기
        dp[i][0] = sticker[i][0]
        if n > 1:
            if i == 0:
                dp[i][1] = sticker[1][0] + sticker[0][1]
            else:
                dp[i][1] = sticker[1][1] + sticker[0][0]

    for j in range(2, n):
        for i in range(2):
            if i == 0:
                dp[i][j] = max(dp[i+1][j-1], dp[i+1][j-2]) + sticker[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j-2]) + sticker[i][j]   
                  

    print(max(dp[0][n-1], dp[1][n-1]))
