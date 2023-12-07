import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(1000010)]
rank = [0 for i in range(1000010)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[b] < rank[a]:
        parent[b] = a
    else:
        parent[a] = b
        rank[b] += 1

for _ in range(m):
    tp, a, b = map(int, input().split())
    if tp == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)