import sys
input = sys.stdin.readline

def isGcd(n, m):
    while m > 0:
        n, m = m, n % m
    return n

N = int(input().strip())

for _ in range(N):
    max_gcd = 1
    test = [int(i) for i in input().split()]
    M = len(test)

    first = 0
    while True:
        if first >= M:
            break
        for i in range(M):
            if first != i:
                gcd = isGcd(max(test[first], test[i]), min(test[first], test[i]))
                if gcd > max_gcd:
                    max_gcd = gcd
        first += 1
    print(max_gcd)
