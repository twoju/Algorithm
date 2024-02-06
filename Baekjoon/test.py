import sys
input = sys.stdin.readline

def recur(cur, total):
    global cnt
    if cur == n:
        if total == s:
            cnt += 1
        return
    recur(cur + 1, total + arr[cur])
    recur(cur + 1, total)

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
recur(0, 0)

if s == 0:
    cnt -= 1
print(cnt)