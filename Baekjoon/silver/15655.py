def recur(cur, start):
    if cur == m:
        print(*res)
        return
    for i in range(start, n):
        if selected[i]:
            continue
        res[cur] = arr[i]
        selected[i] = True
        recur(cur + 1, i + 1)
        selected[i] = False


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

res = [0] * m
selected = [False] * n
recur(0, 0)