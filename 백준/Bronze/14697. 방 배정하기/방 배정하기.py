import sys
input = sys.stdin.readline

a, b, c, n = map(int, input().split())

for i in [a, b, c]:
    if n % i == 0:
        print(1)
        sys.exit(0)

for i in range(n // a + 1):
    for j in range(n // b + 1):
        for k in range(n // c + 1):
            if a * i + b * j + c * k == n:
                print(1)
                sys.exit(0)

print(0)