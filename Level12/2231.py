n = int(input())
result = 0
for i in range(1, n+1):
    result = i
    for j in range(len(str(i))):
        result += int(str(i)[j])
    if result == n:
        print(i)
        break
    # 생성자가 없을 경우는?
    if i == n:
        print(0)
