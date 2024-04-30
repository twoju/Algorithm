import sys
input = sys.stdin.readline

def recur(cur):
    if cur == m:
        print(*selected)
        return
    for nxt in range(1, n + 1):
        selected[cur] = nxt
        recur(cur + 1)

n, m = map(int, input().split())
selected = [0] * m
recur(0)