import sys
input = sys.stdin.readline

def recur(cur, C):
    global ans
    if cur == n - 1:
        now = ''
        for c in C:
            now += str(c)
        if int(now) >= B:
            return
        ans = max(ans, int(now))
        return
    for i in range(n):
        nxt = arr[i]
        if visited[i]:
            continue
        visited[i] = 1
        recur(cur + 1, C + [nxt])
        visited[i] = 0

A, B = map(int, input().split())
arr = []
for i in str(A):
    arr.append(int(i))

n = len(str(A))
ans = -1

if len(str(A)) > len(str(B)):
    print(ans)
else:
    visited = [0] * n
    for i in range(n):
        if arr[i] == 0:
            continue
        visited[i] = 1
        recur(0, [arr[i]])
        visited[i] = 0
    print(ans)