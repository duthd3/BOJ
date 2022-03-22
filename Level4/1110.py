num = int(input())
num1 = num
count = 0

while True:
    a = num/10
    b = num%10
    c = (b*10) + ((a+b)%10)
    count+=1
    if c == num1:
        break
    num = c
    
print(count)
