k = int(input())
result = []

for i in range(k):
    input_data = int(input())
    if input_data == 0:
        result.pop()
    else:
        result.append(input_data)
print(sum(result))
