#모든 프로그램은 적절한 입출력 양식을 가지고 있습니다.
#프로그램 동작의 첫 번째 단계는 데이터를 입력 받거나 생성하는 것입니다.
import sys

#input() 함수는 한 줄의 문자열을 입력 받는 함수입니다.
#map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용합니다.

#n=int(input())
#data = list(map(int, input().split()))

#data.sort(reverse=True)
#print(data)



#data = input()
#print(data)


#n, m, k = map(int, input().split())

#print(n, m, k)

#빠르게 입력 받기
#사용자로부터 입력을 최대한 빠르게 받아야 하는 경우가 있습니다.
#파이썬의 경우 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 메서드를 이용합니다.
#단, 입력 후 엔터가 줄 바꿈 기호로 입력되므로 rstrip()메서드를 함께 사용합니다.

#data = sys.stdin.readline().rstrip()
#print(data)

a = 1
b= 2
print(a, b)
print(7, end= " ")
print(8, end=" ")

answer = 7
print("정답은 "+ str(answer) + "입니다.")








