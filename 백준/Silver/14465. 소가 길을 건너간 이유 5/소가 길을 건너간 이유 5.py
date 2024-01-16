import sys
input = sys.stdin.readline

n, k, b = map(int, input().split())
cross = [i for i in range(1, n + 1)]

for _ in range(b):
    e = int(input().strip())
    cross[e - 1] = -1

cnt = 0
for i in range(k):
    if cross[i] == -1:
        cnt += 1

ans = cnt
for i in range(1, n - k + 1):
    if cross[i - 1] == -1:
        ans -= 1
    if cross[i + k - 1] == -1:
        ans += 1
    cnt = min(ans, cnt)

print(cnt)