import sys

def recur(arr, p, f, s, v, c):
    global price, ans
    if c >= price:
        return
    if p >= nutri[0] and f >= nutri[1] and s >= nutri[2] and v >= nutri[3]:
        if c < price:
            price = c
            ans = [i for i in arr]
            return
        return
    for i in range(n):
        if selected[i]:
            continue
        arr.append(i + 1)
        selected[i] = True
        recur(arr, p + foods[i][0], f + foods[i][1], s + foods[i][2], v + foods[i][3], c + foods[i][4])
        selected[i] = False
        arr.pop()


n = int(sys.stdin.readline())
nutri = list(map(int, sys.stdin.readline().split()))
foods = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

selected = [False] * n
price = 100000
ans = []
recur([], 0, 0, 0, 0, 0)

if len(ans) == 0:
    print(-1)
else:
    print(price)
    print(*ans)