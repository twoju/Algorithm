import sys
input = sys.stdin.readline

n = int(input())
graph = {}

for i in range(n):
    root, left, right = map(str, input().split())
    graph[root] = (left, right)

def pre_dfs(cur):
    print(cur, end='')
    for nxt in graph[cur]:
        if nxt == '.':
            continue
        pre_dfs(nxt)


def ind_dfs(cur):
    if cur != '.':
        ind_dfs(graph[cur][0])
        print(cur, end='')
        ind_dfs(graph[cur][1])


def post_dfs(cur):
    for nxt in graph[cur]:
        if nxt == '.':
            continue
        post_dfs(nxt)
    print(cur, end='')


pre_dfs('A')
print()
ind_dfs('A')
print()
post_dfs('A')
