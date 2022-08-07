in_ = int(input())


arr = []
for i in str(in_):
    arr.append(int(i))
    
arr.sort(reverse=True)

for i in arr:
    print(i, end="")
