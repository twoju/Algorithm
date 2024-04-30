import sys
input = sys.stdin.readline

def recur(cur, prev):
    if cur == m:
        print(*selected)
        return
    for idx in range(prev, n):
        if arr[idx] < arr[prev]:
            continue
        nxt = arr[idx]
        selected[cur] = nxt
        recur(cur + 1, idx)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

selected = [0] * m
recur(0, 0)