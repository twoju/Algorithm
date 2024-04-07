import sys
input = sys.stdin.readline

n, m = map(int, input().split())
box = [0] * (n + 1)
for _ in range(m):
    i, j, k = map(int, input().split())
    for cur in range(i, j + 1):
        box[cur] = k

print(*box[1:])