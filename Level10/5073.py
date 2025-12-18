
while True:
    arr = list(map(int, input().split()))
    arr.sort()
    a, b, c = arr # a b c 는 크기순으로 정렬
    if a == 0 and b == 0 and c == 0:
        break
    if c >= a + b: # 삼각형의 조건에 부합하지 않는다면
        print("Invalid")
    else:
        if a == b == c:
            print("Equilateral")
        elif a != b and b != c and a != c:
            print("Scalene")
        else:
            print("Isosceles")
