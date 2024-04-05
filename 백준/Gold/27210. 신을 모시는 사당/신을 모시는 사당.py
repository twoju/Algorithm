import sys
input = sys.stdin.readline

n = int(input().strip())
pref_sum = [0] * (n + 1)
arr = list(map(int, input().split()))
for i in range(1, n + 1):
    pref_sum[i] = pref_sum[i - 1] + (1 if arr[i - 1] == 1 else -1)

ans = abs(max(pref_sum) - min(pref_sum))
print(ans)