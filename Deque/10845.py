import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    command = list(sys.stdin.readline().split())
    # push
    if command[0] == "push":
        queue.append(command[1])
    # pop
    elif command[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print("-1")
    # size
    elif command[0] == "size":
        print(len(queue))
    # empty
    elif command[0] == "empty":
        if queue:
            print("0")
        else:
            print("1")
    # front
    elif command[0] == "front":
        if queue:
            q = queue.popleft()
            print(q)
            queue.appendleft(q)
        else:
            print("-1")
    # back
    else:
        if queue:
            q = queue.pop()
            print(q)
            queue.append(q)
        else:
            print("-1")
