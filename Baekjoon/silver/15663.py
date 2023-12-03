def recur(cur):
    if cur == m:
        print(' '.join(map(str, ans)))
        return
    used = 0
    for i in range(n):
        if selected[i]:
            continue
        if used == arr[i]:
            continue
        ans.append(arr[i])
        used = arr[i]
        selected[i] = True
        recur(cur + 1)
        selected[i] = False
        ans.pop()

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

selected = [False] * n
ans = []

recur(0)