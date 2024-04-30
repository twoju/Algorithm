import sys
input = sys.stdin.readline

n, m, l, k = map(int, input().split())
stars = []
x = set()
y = set()
for _ in range(k):
    a, b = map(int, input().split())
    stars.append((a, b))
    x.add(a)
    y.add(b)

ans = k
for i in x:
    for j in y:
        cnt = k
        for dx, dy in stars:
            if dx <= i + l and dy <= j + l and dx >= i and dy >= j:
                cnt -= 1

        ans = min(cnt, ans)

print(ans)