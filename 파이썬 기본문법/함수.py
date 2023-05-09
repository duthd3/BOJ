# 함수
# 함수란 특정한 작업을 하나의 단위로 묶어놓은 것을 의미합니다.
# 함수를 사용하면 불필요한 소스코드의 반복을 줄일 수 있습니다.
# 내장함수: 파이썬이 기본적으로 제공하는 함수
# 사용자 정의 함수: 개발자가 직접 정의하여 사용할 수 있는 함수

def add(a, b):
    return a + b
print(add(3, 5))

def add2(a, b):
    print("함수의 결과: ", a + b)
add2(3, 7)
add(2,5)

def subtract(a, b):
        return a - b
result = subtract(7, 3)
print(result)

# 파이썬에서 함수는 여러 개의 반환 값을 가질 수 있습니다.
def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a/ b
    return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(7, 3)
print(a, b, c, d)


