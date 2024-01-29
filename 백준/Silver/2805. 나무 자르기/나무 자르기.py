N, M = map(int, input().split())

tree = sorted(list(map(int, input().split())))

# tree에서 큰 나무부터 자르기 체크
# tree 에서 mid 보다 큰게 있으면 sum += i - mid
# if sum >= M: break, print(bottom)
top, bottom = 1, max(tree)

while top <= bottom:
    mid = (top + bottom) // 2
    sum = 0
    for i in tree:
        if i > mid:
            sum += i - mid
    if sum < M:
        bottom = mid - 1
    else:
        top = mid + 1

print(bottom)