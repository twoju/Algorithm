import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def recur(cur):
    if cur == m:
        print(*ans)
        return
    for i in arr:
        if visited[i]: continue
        ans[cur] = i
        visited[i] = True
        recur(cur + 1)
        visited[i] = False
    
ans = [0] * m
visited = [False] * 10001
recur(0)