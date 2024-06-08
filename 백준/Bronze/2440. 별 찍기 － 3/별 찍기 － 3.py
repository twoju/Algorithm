import sys
input = sys.stdin.readline

n = int(input().strip())

for i in range(n, 0, -1):
    for _ in range(i):
        print('*', end='')
    print('')