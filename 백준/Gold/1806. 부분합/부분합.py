import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

pref_sum = [0] * (n + 1)
for i in range(1, n + 1):
    pref_sum[i] = pref_sum[i - 1] + arr[i - 1]

ans = 100001
l, r = 0, 1
while l < n:
    total = pref_sum[r] - pref_sum[l]
    if total >= s:
        ans = min(ans, r - l)
        l += 1
    else:
        if r >= n:
            l += 1
        else:
            r += 1
    
if ans == 100001:
    print(0)
else:
    print(ans)