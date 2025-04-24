import math
# 1 4 16 64 256
# 2**2 3**2 5**2 9**2
n = int(input())
answer = 1
for i in range(0, n):
    answer *= 4
print(int((math.sqrt(answer) + 1) ** 2))
