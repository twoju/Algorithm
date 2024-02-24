import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input().strip())
price = list(map(int, input().split()))
sales = defaultdict(list)

for i in range(1, n + 1):
    p = int(input().strip())
    for j in range(p):
        a, d = map(int, input().split())
        sales[i].append((a, d))

def recur(cur):
    global order
    if cur == n:
        order.append(res[:])
        return
    for i in range(1, n + 1):
        if visited[i]:
            continue
        visited[i] = True
        res[cur] = i
        recur(cur + 1)
        visited[i] = False


order = []
res = [0] * n
visited = [False] * (n + 1)
recur(0)

ans = sum(price)
for now in order:
    total = price[:]
    tmp = 0
    for i in now:
        tmp += total[i - 1]
        for a, d in sales[i]:
            total[a - 1] = max(1, total[a - 1] - d)
    ans = min(ans, tmp)

print(ans)