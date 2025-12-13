# 색종이 넓이 = 100
# 색종이의 갯수 * 100에서 겹쳐진 넓이만 빼주면 된다
n = int(input())
board = [[0] * 100 for _ in range(100)]
result = 0
for i in range(n):
    x, y = map(int, input().split())
    
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if board[j][i] != 1: # x,y 구분이 의미가 크지는 않음.
                board[j][i] = 1
                result += 1
print(result)
