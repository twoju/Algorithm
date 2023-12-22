import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    location = list(map(int, input().split()))

    print((max(location) - min(location)) * 2)