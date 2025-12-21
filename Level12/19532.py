# x + 3y = -1
# 4x + y = 7

# x + 3y = -1
# 12x + 3y = 21

a, b, c, d, e, f = list(map(int, input().split()))
x = (e*c - b*f) // (e*a - b*d)
y = (a*f - d*c) // (a*e - d*b)

print(x, y)
