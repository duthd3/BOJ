board = [list(map(int, input().split())) for _ in range(9)]

max_value = 0
x = 0
y = 0
for i in range(9):
    # 최대값이 갱신 될 때만 인덱스를 따오면 됨
    if max_value <= max(board[i]):
        max_value = max(board[i])
        x = i + 1
        y = board[i].index(max_value) + 1

print(max_value)
print(x, y)
