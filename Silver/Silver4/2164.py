from collections import deque
n = int(input())

dq = deque()

for i in range(n, 0, -1):
    dq.append(i)
    


while len(dq)!=1:
    dq.pop()
    dq.rotate(1)
    
print(dq[0])
