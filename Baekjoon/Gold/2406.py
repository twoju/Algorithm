import sys
input = sys.stdin.readline

# n 노드 수, m 간선의 수
n, m = map(int, input().split())
network = [i for i in range(n + 1)]

def find(x):
    if network[x] != x:
        network[x] = find(network[x])
    return network[x]

def union(a, b):
    a = find(a)
    b = find(b)
    network[b] = a

for _ in range(m):
    u, v = map(int, input().split())
    union(u, v)

connect_cost = [list(map(int, input().split())) for _ in range(n)]
mst = []

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            continue
        mst.append([connect_cost[i][j], i + 1, j + 1])

mst.sort()

min_cost = 0
ans = []

for cost, i, j in mst:
    fi = find(i)
    fj = find(j)
    if fi != fj:
        if fi > fj:
            network[fi] = fj
        else:
            network[fj] = fi
        ans.append((i, j))
        min_cost += cost

print(min_cost, len(ans))
for computer in ans:
    print(*computer)
    