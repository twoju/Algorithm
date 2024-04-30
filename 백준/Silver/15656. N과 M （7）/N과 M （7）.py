import sys
input = sys.stdin.readline

def recur(cur):
    if cur == m:
        print(*selected)
        return
    for nxt in arr:
        selected[cur] = nxt
        recur(cur + 1)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

selected = [0] * m
recur(0)