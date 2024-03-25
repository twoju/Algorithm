import sys
input = sys.stdin.readline

def check(cur):
    global cnt
    if cur == n:
        cnt += 1
        return
    if cur > n:
        return
    for nxt in range(1, 4):
        if cur + nxt > n:
            continue
        check(cur + nxt)


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    cnt = 0
    check(0)
    print(cnt)