import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(cur, arr):
    visited[cur] = True
    arr.add(cur)
    
    for i in number[cur]:
        if i not in arr:
            dfs(i, arr.copy())
        else:
            ans.extend(list(arr))
            return

n = int(input())
number = [[] for _ in range(0, n + 1)]

for i in range(n):
    a = int(input())
    number[a].append(i + 1)

ans = []
visited = [False] * (n + 1)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, set([]))

ans.sort()
print(len(ans))
for i in ans:
    print(i)