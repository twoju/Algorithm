import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def recur(cur):
    global ans
    if cur == m:
        print(*ans)
        return
    for i in range(1, n + 1):
        ans[cur] = i
        recur(cur + 1)

ans = [0] * m
recur(0)