import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))
x = int(input().strip())

arr.sort()
l, r = 0, n - 1
ans = 0
while l < r:
    total = arr[l] + arr[r]
    if total == x:
        ans += 1
    
    if total <= x:
        l += 1
    else:
        r -= 1

print(ans)