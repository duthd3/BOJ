# 방번호

input_data = list(map(int, input()))

check_array = [0] * 10

not_six_nine_max_count = 0
six_nine_count = 0 # 6, 9개수
six_nine_array = [] # 6 , 9 담을 배열
e_array = []
for i in input_data:
    if i == 6 or i == 9:
        six_nine_array.append(i)
    else:
        check_array[i] += 1
max_count = max(check_array)
if len(six_nine_array) % 2 == 0:
    six_nine_count = len(six_nine_array) // 2
else:
    six_nine_count = (len(six_nine_array) + 1) // 2

print(max(max_count, six_nine_count))

# 6과 9는 뒤집어서 사용할 수있다. 즉, 나온 횟수를 기록할 때 6과 9가 중요한게 아니라 그냥 카운트가 6한번 9한번 이런식으로 반복해서 들어가기만 하면됨

#for i in num:
#    if i == 6 or i == 9:
        # 여기가 바로 번갈아가면서 카운트 증가시킬 수 있는 로직
#        if checked[6] <= checked[9]:
#            checked[6] += 1
#        else:
#            checked[9] += 1
#    else:
#        checked[i] += 1
