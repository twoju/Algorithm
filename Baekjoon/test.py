import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input().strip())
A = list(map(int, input().split()))

ans = [0]
# bisect_left 사용하는 방법
# for cur in A:
#     if cur > ans[-1]:
#         ans.append(cur)
#     else:
#         idx = bisect_left(ans, cur)
#         ans[idx] = cur

# bisect 없이 구현하는 방법
for cur in A:
    if cur > ans[-1]:
        ans.append(cur)
    else:
        s, e = 0, len(ans)
        while s < e:
            mid = (s + e) // 2
            if ans[mid] < cur:
                s = mid + 1
            else:
                e = mid
        ans[e] = cur

print(len(ans) - 1)