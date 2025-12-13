n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for i in range(n)]
answer = [[c + d for c, d in zip(e, f)] for e, f in zip(a, b)]

for row in range(n):
    for col in range(m):
        print(answer[row][col], end = ' ')
    print()
