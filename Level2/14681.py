x = int(input())
y = int(input())

# x가 양수일때(1, 4 사분면)
if x>0:
    # y도 양수일때(1사분면)
    if y>0:
        print(1)
    else:
        print(4)    
# x가 음수일때(2, 3 사분면)
if x<0:
    if y>0:
        print(2)
    else:
        print(3)