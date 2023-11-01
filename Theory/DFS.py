"""
DFS : 깊이 우선 탐색 (핵심은 연결 요소를 구하기)

- 시작 노드의 연결요소를 모두 탐색한다
"""

# 바이러스 - 인접 리스트 만들기

def dfs(cur):
    cnt = 1
    visitied[cur] = True
    for nxt in graph[cur]:
        if visitied[nxt]:
            continue
        cnt += dfs(nxt)
    return cnt

n = input()
m = input()
cnt = 0
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visitied = [False] * (n + 1)
for i in range(1, n + 1):
    if not visitied[i]:
        dfs(i)
        cnt += 1


# ---

# 단지 번호 붙이기 flood fill

def dfs(x, y):
    global size
    visitied[x][y] = True
    size += 1
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if visitied[nx][ny]:
            continue
        if visitied[nx][ny] == 0:
            continue
        dfs(nx, ny)


n = input()
board = [list(map(int, input())) for _ in range(n)]
visitied = [[False] * n for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cnt = 0
tmp = []

for i in range(n):
    for j in range(n):
        # board 에 있고, 방문한 적 없으면
        if board[i][j] == 1 and not visitied[i][j]:
            cnt += 1
            tmp.append(dfs(i, j))

tmp.sort()
print(cnt)


# 유탁님 코드
import sys
input = sys.stdin.readline



def dfs(x, y):
    global size
    visited[x][y] = True
    size += 1
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if visited[nx][ny]:
            continue
        if board[nx][ny] == 0:
            continue
        dfs(nx, ny)


n = int(input())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cnt = 0
tmp = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            cnt += 1
            size = 0
            dfs(i, j)
            tmp.append(size)
tmp.sort()
print(cnt)
for i in tmp:
    print(i)