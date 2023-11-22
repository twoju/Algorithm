import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

chicken = []
home = []
board = []
for col in range(n):
    city = list(map(int, input().split()))
    board.append(city)

    for row in range(n):
        if city[row] == 2:
            chicken.append((col, row))
        if city[row] == 1:
            home.append((col, row))

def check(chicken, home):
    distance = abs(chicken[0] - home[0]) + abs(chicken[1] - home[1])
    return distance

q = deque()
dist = [[0 for _ in range(len(chicken))] for _ in range(len(home))]

for i in range(len(home)):
    for j in range(len(chicken)):
        visited = [[False] * n for _ in range(n)]
        q.append(chicken[j])

        while q:
            x, y = q.popleft()
            # 집 도착하면 이 치킨집에서 갈 수 있는 치킨거리에 더해주기
            if x == home[i][0] and y == home[i][1]:
                dist[i][j] = check(chicken[j], home[i])
                break
            for nxt in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dx, dy = x + nxt[0], y + nxt[1]
                if dx < 0 or dy < 0 or dx >= n or dy >= n:
                    continue
                if visited[dx][dy]:
                    continue
                q.append((dx, dy))
                visited[dx][dy] = True


def recur(cur, s):
    if cur == m:
        arr.append(res[:])
        return
    for i in range(s, len(chicken)):
        if selected[i]:
            continue
        res[cur] = i
        selected[i] = True
        recur(cur + 1, i + 1)
        selected[i] = False

ans = 1e9

res = [0] * m
selected = [False] * len(chicken)
arr = []
recur(0, 0)

for nxt in arr:
    cnt = 0
    for i in range(len(home)):
        min_val = 1e9
        for j in nxt:
            min_val = min(min_val, dist[i][j])
        cnt += min_val
    ans = min(ans, cnt)

print(ans)