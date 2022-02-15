A, B = input().split(" ")
C = int(input())
A = int(A)
B = int(B)

mok = (B + C)//60
na = (B+C)%60

print((A+mok)%24, na)


