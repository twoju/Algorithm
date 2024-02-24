import sys
input = sys.stdin.readline
from collections import defaultdict

n, m, k = map(int, input().split())
skills = [list(map(int, input().split())) for _ in range(m)]

def recur(cur, cnt):
    global ans
    if cur == m:
        if len(d) <= n:
            ans = max(ans, cnt)
        return
    if len(d) > n:
        return
    for i in range(k):
        d[skills[cur][i]] += 1
    recur(cur + 1, cnt + 1)
    for i in range(k):
        d[skills[cur][i]] -= 1
        if d[skills[cur][i]] == 0:
            d.pop(skills[cur][i])
    recur(cur + 1, cnt)
    
ans = 0
d = defaultdict(int)
recur(0, 0)
print(ans)