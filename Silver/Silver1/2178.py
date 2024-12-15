from collections import deque
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0] # 상 하
dy = [0, 0, -1, 1] # 좌 우

# bfs
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    # 큐가 비어질 떄 까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4): # 상 하 좌 우 확인하기
            nx = x + dx[i]
            ny = y + dy[i]
            # 조건 생각하기
            # 1. 그래프를 벗어나면 
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 2. 0일경우
            if graph[x][y] == 0:
                continue
            # 3. 갈 수 있는 경우라면
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0,0))
