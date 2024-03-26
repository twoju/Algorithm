import sys
input = sys.stdin.readline

n, k = map(int, input().split())

if n == k:
    print('Impossible')
elif n == k + 1:
    for i in range(1, n + 1):
        print(i, end=' ')
else:
    print(k + 2, end=' ')
    for i in range(2, k + 2):
        print(i, end=' ')
    for i in range(k + 2, n + 1):
        print(i + 1 if i < n else 1, end=' ')