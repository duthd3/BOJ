N, K = map(int, input().split()) # N:물품의 수, K: 가방에 넣을 최대 무게

# 1.현재 배낭의 허용 무게보다 넣을 물건의 무게가 더 크다면 넣지 않는다.
# 2.그렇지 않다면, 다음중 더 나은 가치를 선택하여 넣는다.
# 2-1)현재 넣을 물건의 무게만큼 배낭에서 뺀다. 그리고 현재 물건을 넣는다.
# 2-2)현재 물건을 넣지않고 이전 배낭 그대로 가지고 간다.

thing = [[0,0]] # 담을 물건의 무게와 가치를 저장할 배열
d = [[0]*(K+1) for _ in range(N+1)] # 배낭의 최대가치 저장

for i in range(N):
    thing.append(list(map(int, input().split()))) # thing배열에 물건의 무게와 가치 저장

for i in range(1, N+1):
    for j in range(1, K+1):
        w = thing[i][0] # 물건의 무게 추출
        v = thing[i][1] # 물건의 가치 추출
       
        if j<w: # 물건의 무게가 배낭의 현재 허용용량보다 클 때
           d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w] + v)

print(d[N][K]) 
