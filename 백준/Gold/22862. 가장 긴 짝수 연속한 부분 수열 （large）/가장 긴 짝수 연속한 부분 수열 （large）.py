import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
large_odd = [0] * (k + 2)

odd = 0
cnt = 0
r = 0
for l in range(n):
    while r < n:
        if odd > k:
            break
        if arr[r] % 2:
            odd += 1
        else:
            cnt += 1
        r += 1
        large_odd[odd] = max(large_odd[odd], cnt)

    if arr[l] % 2:
        odd -= 1
    else:
        cnt -= 1

print(max(large_odd[:k + 1]))