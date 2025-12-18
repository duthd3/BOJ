# 3개의 막대가 있어
# 삼각형의 조건은 제일 긴 변이 나머지 두변의 합보다 짧아야 함
# 막대의 길이는 줄이는거만 가능

# 제일 긴 변이 나머지 두변의 합보다 크다? 제일 긴 변을 나머지 두변의 합-1로
# 아니다? 3개 그냥 더한거
a, b, c = list(map(int, input().split()))
input_list = [a, b, c]
input_list.sort()

if input_list[0] + input_list[1] <= input_list[-1]:
    print(input_list[0] + input_list[1] + (input_list[0] + input_list[1] - 1))
else:
    print(sum(input_list))    
