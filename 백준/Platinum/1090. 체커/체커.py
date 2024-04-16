import sys
input = sys.stdin.readline

n = int(input().strip())

x = []
y = []
point = []
for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
    point.append((a, b))

ans = [-1] * n
for i in x:
    for j in y:
        dist = []
        for s, e in point:
            d = abs(s - i) + abs(e - j)
            dist.append(d)
        dist.sort()

        cnt = 0
        for k in range(len(dist)):
            cnt += dist[k]
            if ans[k] == -1:
                ans[k] = cnt
            else:
                ans[k] = min(cnt, ans[k])
print(*ans)