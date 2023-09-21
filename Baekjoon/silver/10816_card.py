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


# ans = []

# for i in test:
#     exist = False
#     l = 0
#     r = N - 1

#     while l <= r:
#         mid = (l + r) // 2
#         if card[mid] == i:
#             exist = True
#             break
#         elif card[mid] > i:
#             r = mid - 1
#         else:
#             l = mid + 1
        
#     if exist:
#         ans.append(card.count(i))
#     else:
#         ans.append(0)

# print(*ans)
