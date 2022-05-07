N = int(input())
stack = []
answer = 0

for i in range(N):
    user_input = int(input())
    if user_input != 0 :
        stack.append(user_input)
    else:
        stack.pop()
        
for i in range(len(stack)):
    answer = answer + stack[i]
    
print(answer)
