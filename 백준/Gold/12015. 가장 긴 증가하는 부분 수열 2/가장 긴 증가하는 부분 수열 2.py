import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input().strip())
A = list(map(int, input().split()))

ans = [0]
for cur in A:
    if cur > ans[-1]:
        ans.append(cur)
    else:
        idx = bisect_left(ans, cur)
        ans[idx] = cur

print(len(ans) - 1)