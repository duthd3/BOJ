n, m = list(map(int, input().split()))
group = {}
for i in range(n):
    group_name = input()
    member_count = int(input())
    members = []
    for j in range(member_count):
        member_name = input()
        members.append(member_name)
    group[group_name] = members
# {멤버이름: 그룹}

for i in range(m):
    name = input()
    type = int(input())

    if type == 0:
        for item in sorted(group[name]):
            print(item)
    else:
        print([k for k, v in group.items() if name in v][0])
