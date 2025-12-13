n = int(input())
# 별이 증가하는 부분과
# 별이 감소하는 부분을 나눠서 계산

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2*i - 1))
for j in range(n - 1, 0, -1):
    print(" " * (n - j) + "*" * (2 * j - 1))
    
