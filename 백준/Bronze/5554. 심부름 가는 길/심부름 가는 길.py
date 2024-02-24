import sys
input = sys.stdin.readline

ans = 0
for _ in range(4):
    ans += int(input().strip())

print(ans // 60)
print(ans % 60)