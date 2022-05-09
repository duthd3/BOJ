import sys
input = sys.stdin.readline

N, P = map(int, input().split())
stack = [[] for i in range(7)]
cnt = 0 

for i in range(N):
    jul, plat = map(int, input().split())
    
    if len(stack[jul]) == 0 : #스택이 비어있는 곳의 줄을 누를경우 무조건 추가
        stack[jul].append(plat)
        cnt+=1
        
    else:
        if plat>stack[jul][-1]: #새로운 프랫이 원래있던 프랫보다 큰경우 원래있던 프랫의 손가락을 뗴지않고 새로운 프랫만 눌러주면 된다.
            stack[jul].append(plat)
            cnt+=1    
        elif plat<stack[jul][-1]: # 새로운 프랫이 원래있던 프랫보다 작은경우 새로운 프랫을 누르고 원래있던 프랫에서 손을뗀다(즉, 삭제한다.)
            while True:
                if len(stack[jul])==0 or plat > stack[jul][-1]: # 스택이 비거나 새로운 플랫이 원래있던 플랫보다 크면 손가락 떼는걸 멈춘다.
                    stack[jul].append(plat)
                    cnt+=1
                    break
                elif plat == stack[jul][-1]: # 새로운 플랫과 원래있던 플랫이 같으면 아무것도 하지 않는다.
                    break
                else: # 새로운 플랫이 작으면 원래있던 맨 위 플랫 제거
                    stack[jul].pop()
                    cnt+=1

        
        
print(cnt)
            
    
        
    
    
    
        
