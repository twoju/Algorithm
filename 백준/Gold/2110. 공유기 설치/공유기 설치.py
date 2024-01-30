import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = sorted(list(int(input().strip()) for _ in range(n)))

s, e = 1, max(house) - min(house)
ans = 0
while s <= e:
    mid = (s + e) // 2

    cnt = 1
    now = house[0]

    for i in range(1, n):
        if house[i] >= now + mid:
            cnt += 1
            now = house[i]

    if cnt >= c:
        s = mid + 1
        ans = mid
    else:
        e = mid - 1

print(ans)