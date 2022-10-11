f_str = ' ' + input()
s_str = ' ' + input()

# 기준문자열 하나 잡고 비교할 문자열 하나씩 추가
# 문자열 같으면 왼쪽 대각선 위의 값에 +1
# 문자열이 같지 않으면, 왼쪽의 값과 위쪽의 값 중 큰 값.

dp = [[0]*(len(s_str)) for i in range(len(f_str))]

for i in range(1, len(f_str)):
    for j in range(1, len(s_str)):
        if f_str[i] == s_str[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])

      
print(dp[-1][-1])
