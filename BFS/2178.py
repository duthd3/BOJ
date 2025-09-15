from collections import deque
n, m = map(int, input().split())

board = [list(map(int, input())) for _ in range(n)]


def bfs(x, y):
    queue = deque()
    board[x][y] = 1
    queue.append([x, y])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]


    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < n and nx >= 0 and ny < m and ny >= 0 and board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                queue.append([nx, ny])
    return board

print(bfs(0,0)[-1][-1])

