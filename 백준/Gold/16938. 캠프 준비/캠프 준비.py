import sys
input = sys.stdin.readline

def recur(cur, sol, prev):
    global ans
    if cur > 1:
        if sum(sol) >= l and sum(sol) <= r:
            minn, maxx = min(sol), max(sol)
            if maxx - minn >= x:
                ans += 1
    for i in range(prev + 1, n):
        recur(cur + 1, sol + [level[i]], i)


n, l, r, x = map(int, input().split())
level = sorted(list(map(int, input().split())))
ans = 0

recur(0, [], -1)
print(ans)