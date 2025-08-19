from collections import deque
n = int(input())
result = []
queue = deque()

for i in range(n):
    command = list(input().split())
    if command[0] == 'push_back':
        queue.append(command[1])
    elif command[0] == 'push_front':
        queue.appendleft(command[1])
    elif command[0] == 'front':
        if queue:
            delete = queue.popleft()
            result.append(delete)
            queue.appendleft(delete)
        else:
            result.append(-1)
    elif command[0] == 'back':
        if queue:
            delete = queue.pop()
            result.append(delete)
            queue.append(delete)
        else:
            result.append(-1)
    elif command[0] == 'size':
        result.append(len(queue))
    elif command[0] == 'empty':
        if len(queue) == 0:
            result.append(1)
        else:
            result.append(0)
    elif command[0] == 'pop_front':
        if queue:
            result.append(queue.popleft())
        else:
            result.append(-1)
    elif command[0] == 'pop_back':
        if queue:
            result.append(queue.pop())
        else:
            result.append(-1)

for i in result:
    print(i)
