import sys
from collections import deque
sys.stdin = open('7576_tomato.txt', 'r')

M, N = map(int, sys.stdin.readline().split())
tomato = [[i for i in map(int, sys.stdin.readline().split())] for _ in range(N)]

yes_tomato = deque([])

for i in range(M):
    for j in range(N):
        if tomato[j][i] == 1:
            yes_tomato.append([0, i, j])

dir_x = [0, 1, 0, -1]
dir_y = [-1, 0, 1, 0]

while yes_tomato:
    num, x, y = yes_tomato.popleft()
    for i in range(4):
        dx = x + dir_x[i]
        dy = y + dir_y[i]
        if 0 <= dx < M and 0 <= dy < N and tomato[dy][dx] == 0:
            tomato[dy][dx] = 1
            yes_tomato.append([num + 1, dx, dy])

for i in range(N):
    for j in tomato[i]:
        if j == 0:
            print(-1)
            sys.exit(0)

print(num)
