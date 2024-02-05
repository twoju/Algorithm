import sys
input = sys.stdin.readline

def recur(cur, prev):
    global ans
    if cur == m:
        print(*ans)
        return
    for nxt in range(prev, n):
        ans[cur] = arr[nxt]
        recur(cur + 1, nxt)
    

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = [0] * m
recur(0, 0)