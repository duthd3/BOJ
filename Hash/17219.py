n, m = list(map(int, input().split()))

dict = {}

for i in range(n):
    key, value = input().split()
    dict[key] = value
for j in range(m):
    key = input()
    print(dict[key])
