import sys
input = sys.stdin.readline

def facto(cur, tmp):
    global ans
    if cur == n:
        tmp *= cur
        ans = tmp
        return
    facto(cur + 1, tmp * cur)

n = int(input().strip())
ans = 1
if n == 0 or n == 1:
    print(ans)
    sys.exit(0)
facto(2, 1)
print(ans)