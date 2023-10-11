def select(cur):
    if cur == m:
        print(*selected)
        return
    for i in range(1, n + 1):
        selected[cur] = i
        select(cur + 1)
    

n, m = map(int, input().split())
selected = [0] * m
select(0)