import sys
input = sys.stdin.readline
from collections import defaultdict

def recur(cur, cnt):
    global songs, ans
    if cur == n:
        s_cnt = 0
        for i in range(1, m + 1):
            if d[i]:
                s_cnt += 1
        if s_cnt > songs:
            ans = cnt
            songs = s_cnt
        elif s_cnt == songs:
            ans = min(ans, cnt)
            songs = s_cnt
        return
    for j in range(1, m + 1):
        if info[cur][1][j - 1] == 'Y':
            d[j] += 1
    recur(cur + 1, cnt + 1)
    for j in range(1, m + 1):
        if info[cur][1][j - 1] == 'Y':
            d[j] -= 1
            if d[j] == 0:
                d.pop(j)
    recur(cur + 1, cnt)

n, m = map(int, input().split())
info = [list(map(str, input().split())) for _ in range(n)]
ans = n + 1
songs = 0

d = defaultdict(int)
recur(0, 0)

if songs == 0:
    print(-1)
else:
    print(ans)