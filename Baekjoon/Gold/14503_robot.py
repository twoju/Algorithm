def is_clean():
    global cleaned
    cleaned = [[False] * m for _ in range(n)]
    for r, c in now:
        cleaned[r][c] = True


def get_clean():
    global now
    now = []
    for i in range(n):
        for j in range(m):
            if cleaned[i][j]:
                now.append([i, j])


def clean(r, c):
    if cleaned[r][c] == False:
        now.append([r, c])
        ans += 1
    is_clean()


def find(r, c):
    for i in range(4):
        x = (r + dx[i]) % 4
        y = (c + dy[i]) % 4
        if cleaned[x][y]:
            return 1
    return 0


def move(r, c, d):
    global ans
    ans += 1
    for i in range(4):
        x = r + dx[(d + 3 + i) % 4]
        y = c + dy[(d + 3 + i) % 4]
        if cleaned[x][y] == False:
            r = x
            c = y
            d = (d + 3 + i) % 4
            now.append([r, c, d])


n, m = map(int, input().split())
# row, colum, dir
r, c, d = map(int, input().split())

# 1은 벽이고 0은 청소 안한 칸
state = [list(map(int, input().split())) for _ in range(n)]
# r, c
now = []
cleaned = [[False] * m for _ in range(n)]

cleaned[r][c] = True
ans = 1

# 반시계 방향으로 90도 회전
# dir 북 동 남 서 -> 북 서 남 동 방향으로 돌기
# 회전 하는 것 : (d + 3) % 4
# 뒷 방향으로 가는 경우 (현재 + 2) % 4 하면 된다
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소 안한 칸이면 청소한다
clean(r, c)
# 주변 4칸 탐색
find(d)
# 청소되지 않은 빈 칸이 없는 경우
# if 빈칸 == 0:
#     x, y = move(r, c, d)
#     if state[x][y] == 1:
#         break
#     else:
#         r, c = x, y

print(ans)
