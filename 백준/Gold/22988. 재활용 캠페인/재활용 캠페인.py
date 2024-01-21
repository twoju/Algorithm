import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

brr = []
ans = 0
for i in range(n):
    if arr[i] == x:
        ans += 1
    else:
        brr.append(arr[i])
brr.sort()

l, r = 0, len(brr) - 1
etc = len(brr)
while l < r:
    if brr[l] + brr[r] >= x / 2:
        ans += 1
        l += 1
        r -= 1
        etc -= 2
    else:
        l += 1

print(ans + etc // 3)