import sys
input = sys.stdin.readline

m = int(input().strip())
ball = 1
for _ in range(m):
    a, b = map(int, input().split())
    if a == ball:
        ball = b
    elif b == ball:
        ball = a

print(ball)