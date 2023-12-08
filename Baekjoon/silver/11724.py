import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

for _ in range(m):
    u, v = map(int, input().split())
    if find(u) != find(v):
        union(u, v)

for i in range(1, n + 1):
    find(i)

ans = set(filter(lambda x:x > 0, parent))
print(len(ans))
# def dfs(cur):
#     visited[cur] = True
#     for i in graph[cur]:
#         if not visited[i]:
#             dfs(i)

# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# visited = [False] * (n + 1)

# for _ in range(m):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)

# ans = 0
# for i in range(1, n + 1):
#     if not visited[i]:
#         if not graph[i]:
#             ans += 1
#             visited[i] = True
#         else:
#             dfs(i)
#             ans += 1

# print(ans)

