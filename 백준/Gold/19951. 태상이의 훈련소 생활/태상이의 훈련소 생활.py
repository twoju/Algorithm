import sys
input = sys.stdin.readline

n, m = map(int, input().split())
hi = list(map(int, input().split()))

sign = [0] * 101010
for _ in range(m):
    a, b, k = map(int, input().split())
    sign[a] += k
    sign[b + 1] -= k

for i in range(1, n + 1):
    sign[i] += sign[i - 1]
    hi[i - 1] += sign[i]

print(*hi)
