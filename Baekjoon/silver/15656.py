def recur(cur):
    if cur == m:
        print(*res)
        return
    for i in range(n):
        res[cur] = arr[i]
        recur(cur + 1)


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
res = [0] * m

recur(0)