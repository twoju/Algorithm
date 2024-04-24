import sys
input = sys.stdin.readline

mush = []
for _ in range(10):
    n = int(input().strip())
    mush.append(n)

ans = 0
for m in mush:
    if ans < 100:
        if ans + m >= 100:
            if ans + m - 100 <= 100 - ans:
                ans += m
                break
            break
        ans += m

print(ans)
