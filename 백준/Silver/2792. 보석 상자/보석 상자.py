import sys
input = sys.stdin.readline

n, m = map(int, input().split())
jewel = []
for _ in range(m):
    jewel.append(int(input().strip()))

jewel.sort()

s, e = 1, max(jewel)
while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for j in jewel:
        if j % mid == 0:
            cnt += j // mid
        else:
            cnt += j // mid + 1

    if cnt > n:
        s = mid + 1
    else:
        e = mid - 1

print(s)