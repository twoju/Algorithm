def select(cur, start):
    if cur == m:
        print(*selected)
        return
    for i in range(start, n + 1):
        if visited[i]:
            continue
        selected[cur] = i
        visited[i] = True
        select(cur + 1, i + 1)
        visited[i] = False
    

n, m = map(int, input().split())
selected = [0] * m
visited = [False] * (n + 1)
select(0, 1)