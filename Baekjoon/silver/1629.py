import sys
input = sys.stdin.readline

def program(a, n):
    if n == 1:
        return a % c
    else:
        res = program(a, n // 2)
        if n % 2 == 0:
            return res ** 2 % c
        else:
            return (res ** 2 * a) % c

a, b, c = map(int, input().split())
print(program(a, b))