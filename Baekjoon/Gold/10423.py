import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
parent = [i for i in range(n + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    parent[b] = a

finished = list(map(int, input().split()))
for i in finished:
    parent[i] = 0
cable = []

for _ in range(m):
    u, v, w = map(int, input().split())
    cable.append((w, u, v))

cable.sort(key=lambda x:x[0])

ans = 0
for cost, s, e in cable:
    s, e = find(s), find(e)
    if s != e:
        union(s, e)
        ans += cost

print(ans)