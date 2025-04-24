# 쿼터 25
# 다임 10
# 니켈 5
# 페니 1
# 거스름돈은 항상 500 이하
# 손님이 받는 동전의 개수 최소화
# 즉, 큰거부터 가장 많이 준다
t = int(input())
answer = ""
c = [0, 0, 0, 0] # 쿼터 다임, 니켈, 페니의 개수
for i in range(t):
    m = int(input())
    while True:
        if m >= 25:
            m -= 25
            c[0] += 1
        elif m >= 10 and m < 25:
            m -= 10
            c[1] += 1
        elif m >= 5 and m < 10:
            m -= 5
            c[2] += 1
        elif m >= 1 and m < 5:
            m -= 1
            c[3] += 1
        else:
            break
    for i in c:
       print(i, end=" ")
    c = [0, 0, 0, 0]
