import sys
sys.stdin = open('2304.txt', 'r')

N = int(sys.stdin.readline())

height = [0 for _ in range(1001)]
max_height = [0, 0]
for _ in range(N):
    L, H = map(int, sys.stdin.readline().split())
    if H > max_height[1]:
        max_height = [L, H]
    height[L] = H

ans = 0
now = 0
for i in range(max_height[0] + 1):
    now = max(now, height[i])
    ans += now
now = 0
for i in range(1000, max_height[0], - 1):
    now = max(now, height[i])
    ans += now
print(ans)