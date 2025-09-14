from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * 9

def bfs(x, y):
    width = 1 # 일단 bfs에 들어왔다라는 것은 최소 그림이 1개 있다라는 말
    a[x][y] = 0 # 방문처리

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    que = deque()
    que.append([x, y])

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 조건
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 1:
                que.append([nx, ny])
                a[nx][ny] = 0 # 연결된 방문하지 않은 곳 방문 처리
                width += 1
    return width

cnt = 0
ans = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == 1: # 방문할 수 있는 곳이면
            print(i, j)
            ans = max(bfs(i, j), ans)
            cnt += 1
print(cnt)
print(ans)
