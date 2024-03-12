import sys
input = sys.stdin.readline
from math import lcm
sys.setrecursionlimit(20000)

def dfs(cur, cnt):
    global i
    visited[cur] = True
    if shake[cur] == i:
        return cnt
    elif not visited[shake[cur]]:
        return dfs(shake[cur], cnt + 1)


n = int(input().strip())
shake = [0] + list(map(int, input().split()))

ans = []
visited = [False] * (n + 1)
for i in range(1, n + 1):
    if visited[i]:
        continue
    ans.append(dfs(i, 1))
print(lcm(*ans))