import sys
input = sys.stdin.readline

def recur(cur, prev):
    if cur == m:
        print(*selected)
        return
    for nxt in range(prev + 1, n + 1):
        selected[cur] = nxt
        recur(cur + 1, nxt)

n, m = map(int, input().split())
selected = [0] * m
recur(0, 0)