import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

def dfs(c):
    global cnt, ans
    if ans == cards:
        cnt = min(cnt, c)
        return
    ret = [0] * n
    for i in range(n):
        ret[i] = ans[shake[i] - 1]
    ans = ret[:]
    dfs(c + 1)

n = int(input().strip())
cards = [i for i in range(1, n + 1)]
shake = list(map(int, input().split()))

cnt = 2000000100
ans = [0] * n
for i in range(n):
    ans[i] = cards[shake[i] - 1]
dfs(1)
print(cnt)