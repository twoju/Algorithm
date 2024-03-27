import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n, m = map(int, input().split())
    print(n - 1)
    for _ in range(m):
        a, b = map(int, input().split())