import sys

def recur(cur, arr, p, f, s, v, c):
    global price, ans
    if p >= nutri[0] and f >= nutri[1] and s >= nutri[2] and v >= nutri[3]:
        if c < price:
            price = c
            ans = [i + 1 for i in arr]
            return
        return
    if cur == n:
        return
    if c >= price:
        return
    new = arr
    new.append(cur)
    recur(cur + 1, new, p + foods[cur][0], f + foods[cur][1], s + foods[cur][2], v + foods[cur][3], c + foods[cur][4])
    new.pop()
    recur(cur + 1, arr, p, f, s, v, c)


n = int(sys.stdin.readline())
nutri = list(map(int, sys.stdin.readline().split()))
foods = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

price = 100000
ans = []
recur(0, [], 0, 0, 0, 0, 0)

if len(ans) == 0:
    print(-1)
else:
    print(price)
    print(*ans)