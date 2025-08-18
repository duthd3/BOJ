n = int(input())
stack = []
result = []
for i in range(n):
    command = input().split()
    # command[0] = 명령
    # command[1] = 숫자
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack) == 0:
            result.append("-1")
        else:
            result.append(stack.pop())
    elif command[0] == 'size':
        result.append(len(stack))
    elif command[0] == 'empty':
        if len(stack) == 0:
            result.append("1")
        else:
            result.append("0")
    else:
        if len(stack) == 0:
            result.append("-1")
        else:
            result.append(stack[-1])
for i in result:
    print(i)
