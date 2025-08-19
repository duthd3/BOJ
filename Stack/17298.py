n = int(input())
arr = list(map(int, input().split()))

#for i in range(n):
#    min = 1000000
#    if n-1 == i:
#        print("-1")
#    else:
#        for j in range(i + 1, n):
#            if arr[j] > arr[i]:
#                print(arr[j], end = " ")
#                break
#        else:
#            print("-1", end = " ")
answer = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)
print(*answer)
