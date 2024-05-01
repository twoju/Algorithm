import sys
input = sys.stdin.readline

def recur(cur, prev):
    global ans, R, G, B
    if cur > 1:
        diff = abs(gom[0] - (R // cur)) + abs(gom[1] - (G // cur)) + abs(gom[2] - (B // cur))
        ans = min(ans, diff)
    if cur >= 7:
        return
    if cur == n:
        return
    for i in range(prev + 1, n):
        R, G, B = R + colors[i][0], G + colors[i][1], B + colors[i][2]
        recur(cur + 1, i)
        R, G, B = R - colors[i][0], G - colors[i][1], B - colors[i][2]

n = int(input().strip())
colors = [list(map(int, input().split())) for _ in range(n)]
gom = list(map(int, input().split()))

ans = 1000
R, G, B = 0, 0, 0
recur(0, -1)
print(ans)