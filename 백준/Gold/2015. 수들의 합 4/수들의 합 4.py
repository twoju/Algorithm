import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
pref_sum = [0] * n
pref_sum[0] = arr[0]
for i in range(1, n):
    pref_sum[i] = pref_sum[i - 1] + arr[i]

cnt = 0
idx_dict = defaultdict(list)
for i in range(n - 1, -1, -1):
    sum_dict = pref_sum[i]

    if sum_dict == k:
        cnt += 1

    cnt += len(idx_dict[sum_dict + k])

    idx_dict[sum_dict].append(i)

print(cnt)