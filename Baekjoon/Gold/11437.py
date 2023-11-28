import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(cur, dep):
    visited[cur] = True
    depth[cur] = dep
    for nxt in graph[cur]:
        if visited[nxt]:
            continue
        ans[nxt] = cur
        dfs(nxt, dep + 1)

def lca(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = ans[a]
        else:
            b = ans[b]
    while a != b:
        a = ans[a]
        b = ans[b]
    return a

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

m = int(input())

ans = [0 for _ in range(n + 1)]
depth = [0 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

dfs(1, 0)

for _ in range(m):
    left, right = map(int, input().split())
    print(lca(left, right))
    
    # while True:
    #     if depth[left] == depth[right]:
    #         break
    #     if depth[left] > depth[right]:
    #         left = ans[left]
    #     else:
    #         right = ans[right]

    # while True:
    #     if left == right:
    #         break
    #     left = ans[left]
    #     right = ans[right]

    # print(left)

import sys
sys.setrecursionlimit(int(1e5))
n = int(input())

parent = [0] * (n+1) # 부모 노드 정보
d = [0] * (n+1) # 각 노드까지의 깊이
c = [0] * (n+1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n+1)] # 그래프(graph) 정보

for _ in range(n-1):    
	a,b = map(int,input().split())
	graph[a].append(b)
	graph[b].append(a)

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x,depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 넘기기
            continue
        parent[y] = x
        dfs(y, depth + 1)
        
# A와 B의 최소 공통 조상을 찾는 함수
def lca(a,b):
    # 먼저 깊이(depth)가 동일하도록
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 노드가 같아지도록
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

dfs(1,0) # 루트 노드는 1번 노드

m = int(input())

for i in range(m):
    a,b = map(int,input().split())
    print(lca(a,b))