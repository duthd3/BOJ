# n키로그램 ㅂ재달
# 3, 5 -> 최대한 적은 봉지 갯수
# 먼저 5부터 최대로 들어갈 수 있는걸 정하고, 그다음 3?

n = int(input())
count = 0
# 18 = 5 5 5 3, 333333
# 4 = 5x, 3x
# 6 = 5x, 3 3
# 
if n == 4 or n == 7: # 4 7
    print(-1)
elif n % 5 == 0: # 5
    print(n // 5)
elif (n % 5 == 1 or n % 5 == 3): # 6 8
    print(n // 5 + 1)
elif n % 5 == 2 or n % 5 == 4:
    print(n // 5 + 2)
