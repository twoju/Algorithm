import sys
input = sys.stdin.readline


n = int(input().strip())
info = [list(map(int, input().split())) for _ in range(n)]

ans = [0] * n
for i in range(n):
    k = 1
    for nxt in range(n):
        if nxt == i:
            continue
        if info[nxt][0] > info[i][0] and info[nxt][1] > info[i][1]:
            k += 1

    ans[i] = k

print(*ans)