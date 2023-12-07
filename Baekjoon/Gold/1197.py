import sys
input = sys.stdin.readline

v, e = map(int, input().split())

rnk = [0 for i in range(1000010)]
parent = [i for i in range(1000010)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if rnk[a] < rnk[b]:
        parent[a] = b
    elif rnk[b] < rnk[a]:
        parent[b] = a
    else:
        parent[a] = b
        rnk[b] += 1

edge = [list(map(int, input().split())) for _ in range(e)]
edge.sort(key=lambda x:x[-1])

ans = 0

for a, b, c in edge:
    if find(a) != find(b):
        union(a, b)
        ans += c

print(ans)
