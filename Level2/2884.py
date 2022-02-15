H, M = input().split(" ")
H = int(H)
M = int(M)

if H == 0:
    H=24
    if M>=45:
        H = 0
        M = M-45
    else:
        H = H - 1
        M = 60 + (M-45)
else:
    if M>=45:
        M = M - 45
    else:
        H = H-1
        M = 60 + (M-45)
print(H,M)