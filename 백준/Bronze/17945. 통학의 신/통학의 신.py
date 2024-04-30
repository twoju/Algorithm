import sys
input = sys.stdin.readline

a, b = map(int, input().split())
for i in range(-1000, 1001):
    if (i ** 2) + (2 * a * i) + b == 0:
        print(i, end=" ")