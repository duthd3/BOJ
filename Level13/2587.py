arr = []
mid = 0
avg = 0
for i in range(5):
    arr.append(int(input()))
arr.sort()    
avg = sum(arr) // 5
mid = arr[len(arr) // 2]

print(avg)
print(mid)
