import sys
input = sys.stdin.readline

n = int(input().strip())
f = int(input().strip())

nd = n // 100
ans = nd * 100

while ans % f != 0:
    ans += 1
print(str(ans)[-2:])