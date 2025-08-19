from collections import deque
#첫번째 원소 뽑느다 = popleft
# 왼쪽 한칸 이동은 popleft -> enque
# 오른쪽 이동은? appendleft

queue = deque()

n, m = list(map(int, input().split()))

input_data = list(map(int, input().split()))
result = 0
for i in range(n):
    queue.append(i+1)

for input in input_data:
    while queue.index(input) != 0:
        if queue.index(input) <= len(queue) // 2: # 찾아야 하는 원소가 길이의 반보다 왼쪽에 있을 경우에는 큐를 왼쪽으로
            queue.rotate(-1)
            result += 1
        else:
            queue.rotate(1)
            result += 1
    queue.popleft()

print(result)
