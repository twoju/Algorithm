def recur(cur):
    if cur == m:
        if res[:] not in ans:
            print(*res)
        ans.append(res[:])
        return
    for i in range(n):
        if selected[i]:
            continue
        res[cur] = arr[i]
        selected[i] = True
        recur(cur + 1)
        selected[i] = False

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

selected = [False] * n
res = [0] * m
ans = []

recur(0)