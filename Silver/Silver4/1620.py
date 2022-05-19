import sys
N, M = map(int, input().split(" "))

mon_dict1 = {}
mon_dict2 = {}
mon_num = 1
for i in range(N):
    name = str(sys.stdin.readline()).strip()
    mon_dict1[mon_num] = name
    mon_dict2[name] = mon_num
    mon_num += 1
answer = []

for j in range(M):
    input_answer = str(sys.stdin.readline()).strip()
    try:
        print(mon_dict1[int(input_answer)])
    except:
        print(mon_dict2[input_answer])
