N = int(input())
card = list(map(int, input().split()))

M = int(input())
test = list(map(int, input().split()))

card = sorted(card)

check = {}

for i in card:
    if i in check:
        check[i] += 1
    else:
        check[i] = 1

for i in test:
    if i in check:
        print(check[i], end=' ')
    else:
        print(0, end=' ')