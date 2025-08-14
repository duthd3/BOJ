a = input() # 첫번째 인풋
b = input() # 두번째 인풋
list_b = list(b)
list_a = list(a)
result = 0
for i in list_a: # a의 문자들 순회
    if i in list_b:
        list_b.remove(i)
        result += 1

print(len(list_a) - result + len(list_b))
