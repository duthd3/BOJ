n = int(input())
for i in range(n):
    f, s = input().split()
    list_f = list(f)
    list_s = list(s)
    if len(list_f) == len(list_s):
        for i in range(len(list_f)):
            if list_f[i] in list_s:
                list_s.remove(list_f[i])
        if len(list_s) == 0:
            print("Possible")
        else:
            print("Impossible")
    else:
        print("Impossible")
