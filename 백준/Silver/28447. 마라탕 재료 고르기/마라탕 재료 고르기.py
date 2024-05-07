import sys
input = sys.stdin.readline
from itertools import combinations

def recur(cur, arr):
    global ans
    if len(arr) == k:
        tmp = 0
        for c in combinations(arr, 2):
            tmp += chemi[c[0]][c[1]]
        ans = max(ans, tmp)
        return
    if cur == n:
        return
    recur(cur + 1, arr + [cur])
    recur(cur + 1, arr)

n, k = map(int, input().split())
chemi = [list(map(int, input().split())) for _ in range(n)]
ans = -100000
recur(0, [])
print(ans)