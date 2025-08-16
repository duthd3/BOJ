import sys

n = int(sys.stdin.readline())

heights = list(map(int, sys.stdin.readline().split()))
result =[]
stack = []

for i in range(n):
    while stack:
        if stack[-1][1] > heights[i]: # 수신 가능한 상황
            result.append(stack[-1][0] + 1)
            break
        else: # 수신 가능한 상황이 아니라면
            stack.pop()
    if not stack: # 스택이 비면 레이저를 수신할 탑이 없음
        result.append(0)
    stack.append([i, heights[i]])
print(" ".join(map(str, result)))
