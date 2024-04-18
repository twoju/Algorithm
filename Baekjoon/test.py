import sys
input = sys.stdin.readline

n = int(input().strip())
point = []
x = []
y = []
for _ in range(n):
    a, b = map(int, input().split())
    point.append((a, b))
    x.append(a)
    y.append(b)

x.sort()
y.sort()

ans = 0
for a, b in point:
    ans += abs(a - x[(n - 1) // 2]) + abs(b - y[(n - 1) // 2])
print(ans)