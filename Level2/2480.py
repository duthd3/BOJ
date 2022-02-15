A, B, C = input().split(" ")
A = int(A)
B = int(B)
C = int(C)
price = 0
# 같은 눈이 3개가 나오는 경우
if A==B==C:
     price = 10000+A*1000

# 같은 눈이 2개가 나오는 경우
elif A==B:
    price = 1000 + A*100
elif A==C:
    price = 1000 + A*100
elif B==C:
    price = 1000 + B*100
# 모두 다른 눈이 나오는 경우
else:
    price = max(A, B, C)*100
print(price)
