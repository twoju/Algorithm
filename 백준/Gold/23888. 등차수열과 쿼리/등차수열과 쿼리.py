import sys
input = sys.stdin.readline

a, d = map(int, input().split())
n = int(input().strip())

def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


for _ in range(n):
    t, s, e = map(int, input().split())

    if t == 1:
        i = (e * ((2 * a) + (e - 1) * d)) // 2
        j = ((s - 1) * ((2 * a) + (s - 2) * d)) // 2
        print(i - j)
    else:
        if s == e:
            print(a + (s - 1) * d)
        else:
            print(gcd(a, d))