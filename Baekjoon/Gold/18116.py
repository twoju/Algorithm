import sys

n = int(sys.stdin.readline())
parent = [i for i in range(1000010)]
rnk = [0 for i in range(1000010)]
size = [1 for i in range(1000010)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if rnk[a] < rnk[b]:
        parent[a] = b
        size[b] += size[a]
    elif rnk[b] < rnk[a]:
        parent[b] = a
        size[a] += size[b]
    else:
        parent[a] = b
        rnk[b] += 1
        size[b] += size[a]

for _ in range(n):
    bot = list(map(str, sys.stdin.readline().split()))

    if bot[0] == 'I':
        union(int(bot[1]), int(bot[2]))
    if bot[0] == 'Q':
        res = find(int(bot[1]))
        print(size[res])