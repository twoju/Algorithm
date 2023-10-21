n, m = map(int, input().split())

def isGcd(n, m):
    while m > 0:
        n, m = m, n % m
    return n

gcd = isGcd(n, m)
print(gcd)
print(n//gcd * m)