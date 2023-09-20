N = int(input())
card = sorted(list(map(int, input().split())))
M = int(input())
test = list(map(int, input().split()))

ans = []
for i in test:
    exist = False
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2
        if card[mid] == i:
            exist = True
            break
        elif card[mid] > i:
            right = mid - 1
        else:
            left = mid + 1
    if exist:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)