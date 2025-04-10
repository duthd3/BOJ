input_data = input()
    
first_character = input_data[0]
zero_count = 0
one_count = 0 # 1뭉텅이 개수
    
if first_character == "1":
    one_count += 1
else:
    zero_count += 1
  
for i in range(1, len(input_data)):
    if input_data[i] != input_data[i-1]: # 다르다면 뭉텅이가 발생
        if input_data[i] == "0": # 0 뭉텅이 발생
            zero_count += 1
        else:
            one_count += 1
print(min(zero_count, one_count))
