import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def func(n):
    ans = n
    i = 2
    while True:
        if i > n:
            break
        ans += (n // i) * (i // 2)
        i *= 2
    return ans

print(func(b) - func(a - 1))