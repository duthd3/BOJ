# M내에서 카드의 합을 최대한 크게 만드는 게임

# M을 넘지 않으면서 최대한 가까운 카드 3장 구하기

n, m = list(map(int, input().split()))
card = list(map(int, input().split()))
# n장의 카드에 써져있는 숫자가 주어졌을 때, m을 넘지 않으면서 최대한 가까운 카드 3장구하기
max_value = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if card[i] + card[j] + card[k] > m:
                continue
            max_value = max(max_value, card[i] + card[j] + card[k])

print(max_value)
