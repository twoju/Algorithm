import sys
input = sys.stdin.readline

min_sum = 200000000
a, b = map(int, input().split())
cur = b // a
ans = []

def gcd(a, b):
    if a % b == 0:
        return b

    return gcd(b, a % b)


for i in range(1, int(cur ** 0.5) + 1):
    j = int(cur / i)

    if cur % i == 0 and gcd(i, j) == 1:
        if j - i < min_sum:
            min_sum = j - i
            ans = [i * a, j * a]

print(*ans)