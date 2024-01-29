import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lans = sorted(list(int(input().strip()) for _ in range(k)))

s, e = 1, max(lans)
while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for lan in lans:
        cnt += lan // mid

    if cnt >= n:
        s = mid + 1
    else:
        e = mid - 1

print(e)