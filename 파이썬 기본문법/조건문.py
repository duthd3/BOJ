#조건문
#조건문은 프로그램의 흐름을 제어하는 문법입니다.
#조건문을 이용해 조건에 따라서 프로그램의 로직을 설정할 수 있습니다.

x = 15

if x >= 10:
    print("x >= 10")
if x >= 0:
    print("x >= 0")
if x >= 30:
    print("x >= 30")    


a = -15
if a>=0:
    print("a>=0")
elif a>=-10:
    print("0>a>=-10")
else:
    print("-10>a")
    
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

#비교 연산자
#==, !=, >, <, >=, <=
#논리 연산자
#and, or, not(파이썬은 단어를 직접 입력!)

if True or False:
    print("yes")

a = 15
if a <= 20 and a>=0:
    print("yes")

#파이썬의 기타 연산자
#in연산자, not in 연산자
#x in 리스 => 리스트 안에 x가 들어 있을 때 참이다.
#x not in 문자열 => 문자열 안에 x가 들어가 있지 않을 때 참이다.

#pass 키워드
#아무것도 처리하고 싶지 않을 때 pass 키워드를 사용합니다.


