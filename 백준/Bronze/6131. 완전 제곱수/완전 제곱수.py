import sys
input = sys.stdin.readline

ans = 0
n = int(input())
for b in range(1, 501):
    for a in range(b, 501):
        if (a ** 2) == (b ** 2) + n:
            ans += 1
print(ans)