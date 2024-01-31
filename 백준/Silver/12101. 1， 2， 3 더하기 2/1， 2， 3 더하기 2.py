import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def recur(cur, ans):
    global cnt
    if cur > n:
        return
    if cur == n:
        cnt += 1
        if cnt == k:
            print(ans[:-1])
            sys.exit(0)
        return
    for i in range(1, 4):
        recur(cur + i, ans + str(i) + '+')

cnt = 0
recur(0, '')
print(-1)