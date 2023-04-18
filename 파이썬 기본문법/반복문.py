i = 1
result = 0

while i<=9:
    result += i
    i += 1
print(result)

#for 반복문
#for문의 구조는 다음과 같은데, 특정한 변수를 이용하여 'in' 뒤에 오는 데이터(리스트, 튜플 등)에 포함되어 있는 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문합니다.
#for 변수 in 리스트:
#   실행할 소스코드
array = [9, 8, 7, 6, 5]
for x in array:
    print(x)

#for문에서 연속적인 값을 차례대로 순회할 때는 range()를 주로 사용합니다.
#range(시작 값, 끝 값+1)
#인자를 하나만 넣으면 자동으로 시작 값은 0이 됩니다.

result = 0
for i in range(1, 31):
    result += i
print(result)

result = 0
for i in range(1, 10):
    if i%2 == 0:
        continue
    result += i
print(result)

scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i+1, "번 학생은 합격입니다.")
        

for i in range(2, 10):
    for j in range(1, 10):
        print(i, "x", j, "=", i*j )
