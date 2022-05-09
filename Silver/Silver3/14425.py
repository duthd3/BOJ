N, M = map(int, input().split())

cnt = 0
S = set([input() for i in range(N)])

for i in range(M):
    t = input()
    if t in S:
        cnt+=1
print(cnt)


