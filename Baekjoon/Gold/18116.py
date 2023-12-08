import sys

n = int(sys.stdin.readline())
parent = [i for i in range(1000001)]
size = [1 for i in range(1000001)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
        size[a] += size[b]
    elif b < a:
        parent[a] = b
        size[b] += size[a]

for _ in range(n):
    bot = list(sys.stdin.readline().split())

    if bot[0] == 'I':
        union(int(bot[1]), int(bot[2]))
    else:
        res = find(int(bot[1]))
        print(size[res])