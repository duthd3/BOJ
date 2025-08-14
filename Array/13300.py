# 방 배정
n, k = map(int, input().split())
# s = 0 여자, s = 1 남자
sy_array = []
stu_array = [[0, 0] for _ in range(6)] # [여, 남] * 6
result = 0

for i in range(n):
    # 성별, 학년
    s, y = map(int, input().split())

    stu_array[y-1][s] += 1

for grade in stu_array:
    for num in grade:
        result += num // k
        if num % k:
            result += 1
print(result)

# 학생들을 이중배열로 표현.
# stu_array[0][1] => 1학년 남자
# 각 학년의 성별 학생수 순회 해서 방의 최대 인원크기로 나눈 몫을 구해주고, 나누어떨어지지 않는다면 방1개 추가
