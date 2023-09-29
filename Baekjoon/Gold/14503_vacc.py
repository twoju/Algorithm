def find(r, c):
    for i in range(4):
        x = (r + dx[i]) % 4
        y = (c + dy[i]) % 4
        if cleaned[x][y]:
            return 1
    return 0

n, m = map(int, input().split())
# row, colum, dir
r, c, d = map(int, input().split())

# 1은 벽이고 0은 청소 안한 칸
state = [list(map(int, input().split())) for _ in range(n)]
# r, c
now = []
cleaned = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if state[i][j]:
            cleaned[i][j] = True

cleaned[r][c] = True
now.append([r, c])
ans = 1

# 반시계 방향으로 90도 회전
# dir 북 동 남 서 -> 북 서 남 동 방향으로 돌기
# 회전 하는 것 : (d + 3) % 4
# 뒷 방향으로 가는 경우 (현재 + 2) % 4 하면 된다
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    for r, c in now:
        if find(r, c):
            ans += 1
            for i in range(4):
                d = (d + 3 + i) % 4
                x = r + dx[d]
                y = c + dy[d]
                if x < m and y < n:
                    if cleaned[x][y]:
                        r = x
                        c = y
                        now.append([r, c])
        # 빈칸 없는 경우 (d + 2) % 4
        else:
            x = r + dx[(d + 2) % 4]
            y = c + dy[(d + 2) % 4]
            if state[x][y]:
                break
            else:
                r = x
                c = y
                d = (d + 2) % 4
    break
print(ans)
