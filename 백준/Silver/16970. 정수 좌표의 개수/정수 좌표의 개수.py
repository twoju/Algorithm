import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

cnt = 0

for x in range(n + 1):
    for y in range(m + 1):
        for a in range(n + 1):
            for b in range(m + 1):
                if gcd(abs(x - a), abs(y - b)) + 1 == k:
                    cnt += 1

print(cnt // 2)