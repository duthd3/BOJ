arr = []
for _ in range(3):
    arr.append(int(input()))

if sum(arr) != 180:
    print("Error")
else:
    # 세각이 모두 같을 경우 - arr[1], arr[2]가 모두 angle과 같음
    if arr[1] == arr[0] and arr[2] == arr[0]:
        print("Equilateral")
    # 세각이 모두 다른 경우
    elif arr[1] != arr[0] and arr[1] != arr[2] and arr[0] != arr[2]:
        print("Scalene") 
    else:
        print("Isosceles")
