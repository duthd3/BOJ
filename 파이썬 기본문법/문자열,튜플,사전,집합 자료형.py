# 문자열 변수를 초기화할 때는 큰따옴표("")나 작은 따옴표('')를 이용합니다.

data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

# 문자열 연산
# 문자열 변수에 + 을 이용하면 문자열이 더해져서 연결됩니다.
# 문자열은 특정 인덱스의 값을 변경할 수는 없습니다.

a = "Hello"
b= "World"

print(a + " " + b)

a = "String"
print(a*3)

a = "ABCDEF"
print(a[2:4])
#a[2] = "b" (문자열은 변경 불가능)

#튜플 자료형
#한 번 선언된 값은 변경할 수 없습니다.
#리스트는 대괄호, 튜플은 소괄호를 이용합니다.
#튜플은 리스트에 비해 공간 효율적입니다.

a = (1,2,3,4,5,6,7,8,9)
print(a[3])
print(a[1:4])

#튜플을 사용하면 좋은 경우
#서로 다른 성질의 데이터를 묶어서 관리해야 할 때
#최단 경로 알고리즘에서는(비용, 노드번호)의 형태로 튜플 자료형을 자주 사용합니다.
#데이터의 나열을 해싱의 키 값으로 사용해야 할 때
#튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용될 수 있습니다.
#리스트보다 메모리를 효율적으로 사용해야 할 떄

#사전 자료형(dictionary)
#키와 값의 쌍을 데이터로 가지는 자료형입니다.
#리스트나 튜플이 값을 순차적으로 저장하는 것과는 대비됩니다.
#변경 불가능한 자료형을 키로 사용할 수 있습니다.

data = dict()
data['사과'] = "Apple"
data['바나나'] = "Banana"
data['코코넛'] = "Coconut"

print(data)


if '사과' in data:
    print(" '사과'를 키로 가지는 데이터가 존재합니다.")

#사전 자료형에서는 키와 값을 별도로 뽑아내기 위한 메서드를 지원합니다.
#키 데이터만 뽑아서 리스트로 이용할 때는 keys()함수를 이용합니다.
#값 데이터만을 뽑아서 리스트로 이용할 때는 values()함수를 이용합니다.


key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

for key in key_list:
    print(data[key])
    
a = dict()
a['홍길동'] = 97
a['이순신'] = 98

print(a)

b = {'홍길동':97, '이순신':98}
print(b)
key_list = list(b.keys())
print(key_list)

#집합 자료형
#중복을 허용하지 않습니다.
#순서가 없습니다.
#리스트 혹은 문자열을 이용해서 초기화할 수 있습니다.
#set()함수를 이용합니다.
#데이터 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있습니다.

data = set([1,2,3,4,4,5])
print(data)

data = {1,1,2,3,4,4,5}
print(data)

#합집합(|), 교집합(&), 차지합(-)
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a|b)
print(a&b)
print(a-b)

data = set([1,2,3])
print(data)

#새로운 원소 추가
data.add(4)
print(data)

#새로운 원소 여러 개 추가
data.update([5,6])
print(data)

#특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)

#리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있습니다.
#사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없습니다.
