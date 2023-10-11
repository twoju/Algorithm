def select(cur, start):
    if cur == m:
        print(*selected)
        return
    for i in range(start, n + 1):
        selected[cur] = i
        select(cur + 1, i)
    

n, m = map(int, input().split())
selected = [0] * m
select(0, 1)