n, m = map(int, input().split()) 
si, sj, dr = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))


# dr: 북 동 남 서
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def solve(ci, cj, dr):
    cnt = 0 # 청소한 공간 수
    while True: # 청소기가 더이상 움직이지 못할 경우 종료
        # [1] 현재 위치 청소
        arr[ci][cj] = 2 
        cnt += 1
        # [2] 왼쪽방향으로 순서대로 탐색
        flag = 1
        while flag == 1:
            # 왼쪽부터 네 방향 중 미청소 영역 있는 경우
            for nd in ((dr + 3) % 4, (dr + 2) % 4, (dr + 1) % 4, dr):
                ni, nj = ci + di[nd], cj + dj[nd]
                if arr[ni][nj] == 0: # 미청소 영역이라면
                    ci, cj, dr = ni, nj, nd
                    flag = 0
                    break
            else: # 4방향 모두 미청소 영역 없음 -> 후진
                bi, bj = ci-di[dr], cj-dj[dr]
                # 그 위치가 벽이라면 못가고 종료
                if arr[bi][bj] == 1:
                    return cnt
                else: # 후진하기
                    ci, cj = bi, bj
    return -1

ans = solve(si, sj, dr)
print(ans)
