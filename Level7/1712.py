#A만원의 고정 비용
#B만원의 가변 비용
#노트북 가격 C 만원

A,B,C = (map(int, input().split(" ")))
if B>=C:
    print(-1)
else:
    print(A//(C-B)+1)
