n, m = list(map(int, (input().split())))
board = []
for i in range(n):
    board.append(list(input()))

count = []
# board의 첫번째 칸이 W인 경우

for i in range(n-7): # 전체 보드판에서 8*8 검사
    for j in range(m-7):
        draw_w = 0 # 시작점이 흰색
        draw_b = 0 # 시작점이 검은색
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a+b) % 2 == 0: 
                    if board[a][b] != 'B':
                        draw_b += 1
                    if board[a][b] != 'W':
                        draw_w += 1
                else:
                    if board[a][b] != 'W':
                        draw_b += 1
                    if board[a][b] != 'B':
                        draw_w += 1
        count.append(min(draw_w, draw_b))
print(min(count))
