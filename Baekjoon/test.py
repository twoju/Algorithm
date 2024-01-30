import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def recur(cur):
    if cur == m:
        print(*res)
        return
    for i in range(1, n + 1):
        if visited[i]: continue
        res[cur] = i
        visited[i] = True
        recur(cur + 1)
        visited[i] = False

res = [0] * m
visited = [False] * (n + 1)
recur(0)