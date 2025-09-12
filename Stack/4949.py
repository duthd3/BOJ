# 여는 괄호가 나오면 스택에 추가
# 닫는 괄호가 나왔을 경우,
# 스택이 비어있으면 올바르지 않은 괄호 쌍
# 스택의 top이 짝이 맞지 않는 괄호일 경우 올바르지 않은 괄호 쌍
# 스택의 top이 짝이 맞는 괄호일 경우 pop
# 모든 과정을 끝낸 후 스택에 괄호가 남아있으면 올바르지 않은 괄호 쌍, 남아있지 않으면 올바른 괄호

while True:
    a = input()
    stack = []

    if a == ".":
        break

    for i in a:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")" or i == "]":
            if stack:
                if (i == ")" and stack[-1] == "(") or i == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    if i == ")" or i == "]":
                        stack.append(i)
                        break
            else:
                stack.append(i)
                break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")
