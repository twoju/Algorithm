import sys
input = sys.stdin.readline 
import heapq

t = 1
while True:
    n = int(input().strip())
    if n == 0:
        break
    crave = [list(map(int, input().split())) for _ in range(n)]
    dist = [[1e9] * n for _ in range(n)]
    q = []
    heapq.heappush(q, (0, 0, crave[0][0]))
    dist[0][0] = crave[0][0]
    ans = 0

    while q:
        x, y, money = heapq.heappop(q)
        if x == n - 1 and y == n - 1:
            ans = money
            break
        for dxy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            dx = x + dxy[0]
            dy = y + dxy[1]
            if dx < 0 or dy < 0 or dx >= n or dy >= n:
                continue
            if dist[dx][dy] <= money + crave[dx][dy]:
                continue
            heapq.heappush(q, (dx, dy, money + crave[dx][dy]))
            dist[dx][dy] = money + crave[dx][dy]

    print(f'Problem {t}: {ans}')
    t += 1