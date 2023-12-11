import sys
input = sys.stdin.readline

n = int(input())
well = []
for i in range(1, n + 1):
    w = int(input())
    well.append([w, 0, i])

for i in range(1, n + 1):
    connect = list(map(int, input().split()))
    for j in range(1, n + 1):
        if i != j:
            well.append([connect[j - 1], i, j])

ans = 0
parent = [i for i in range(n + 1)]
well.sort(key=lambda x:x[0])

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

for cost, i, j in well:
    i = find(i)
    j = find(j)
    if i != j:
        union(i, j)
        ans += cost

print(ans)