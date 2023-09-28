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
    is_clean()


def find(d):
    global ans
    for i in range(len(now)):
        x = now[i][0]
        y = now[i][1]
    for _ in range(4):
        x = (x + d + 3) % 4
        y = (y + d + 3) % 4
        if cleaned[x][y] == False:
            now.append([x, y])
            is_clean()
            ans += 1
            break




def move(r, c, d):
    # 뒷 칸이 0이면 후진하고 clean으로 돌아가기
    # 뒷 칸이 1이면 작동 멈춤
    x = r + dx[(d + 2) % 4]
    y = c + dy[(d + 2) % 4]
    return x, y


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
