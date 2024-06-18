import sys
input = sys.stdin.readline

n = int(input().strip())
ans = 0

for i in range(2, int(n / 2) + 1):
    ans += (n // i - 1) * i

print(ans % 1000000)