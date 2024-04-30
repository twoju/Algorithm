import sys
input = sys.stdin.readline

n = int(input())
if n < 6:
    print(0)
    sys.exit(0)

cnt = 0
for i in range(2, n - 3, 2):
    cnt += (n - i - 2) // 2
print(cnt)
