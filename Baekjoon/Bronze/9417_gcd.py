import sys
sys.stdin = open('9417_gcd.txt', 'r')

N = int(sys.stdin.readline())

def isGcd(n, m):
    while m > 0:
        n, m = m, n % m
    return n

for _ in range(N):
    max_gcd = 1
    test = [int(i) for i in sys.stdin.readline().split()]
    M = len(test)

    first = 0
    while first < M:
        for i in range(M):
            if first != i:
                gcd = isGcd(max(test[first], test[i]), min(test[first], test[i]))
                if gcd > max_gcd:
                    max_gcd = gcd
        first += 1
    print(max_gcd)
