import sys
input = sys.stdin.readline

a, b, n, w = map(int, input().split())
lamb, goat = 0, 0

for i in range(1, n):
    g = n - i
    if (a * i) + (b * g) == w:
        if lamb == 0 and goat == 0:
            lamb, goat = i, g
        else:
            print(-1)
            sys.exit(0)

if lamb != 0 and goat != 0:
    print(lamb, goat)
else:
    print(-1)