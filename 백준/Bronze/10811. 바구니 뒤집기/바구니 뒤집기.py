import sys
input = sys.stdin.readline

n, m = map(int, input().split())
basket = list(i for i in range(n + 1))
for _ in range(m):
    i, j = map(int, input().split())
    basket = basket[:i] + basket[i:j+1][::-1] + basket[j+1:]

print(*basket[1:])