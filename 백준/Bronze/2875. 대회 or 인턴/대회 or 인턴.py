import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
ans = n//2
extra = n % 2

if m < ans:
    extra += (ans - m) * 2
    ans = m
else:
    extra += m - ans

if extra < k:
    if (k - extra) % 3 != 0:
        ans -= ((k - extra) // 3) + 1
    else:
        ans -= (k - extra) // 3

print(ans)