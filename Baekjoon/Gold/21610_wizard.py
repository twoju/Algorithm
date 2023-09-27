def get_is_cloud():
    global is_cloud
    is_cloud = [[False] * N for _ in range(N)]
    for x, y in cloud:
        is_cloud[x][y] = True

def get_cloud():
    global cloud
    cloud = []
    for x in range(N):
        for y in range(N):
            if is_cloud[x][y]:
                cloud.append([x, y])

def move_rain(d: int, s: int):
    for i in range(len(cloud)):
        x = cloud[i][0]
        y = cloud[i][1]
        for _ in range(s):
            x = (x + dx[d] + N) % N
            y = (y + dy[d] + N) % N
        cloud[i][0] = x
        cloud[i][1] = y
    get_is_cloud()
    for i in range(N):
        for j in range(N):
            if is_cloud[i][j]:
                basket[i][j] += 1

def water_copy():
    copy_basket = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            copy_basket[i][j] = basket[i][j]
    for i in range(N):
        for j in range(N):
            if not is_cloud[i][j]:
                continue
            for k in range(4):
                nx = i + dx2[k]
                ny = j + dy2[k]
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                if copy_basket[nx][ny] != 0:
                    basket[i][j] += 1

def make_cloud():
    global cloud
    cloud = []
    for i in range(N):
        for j in range(N):
            if basket[i][j] >= 2 and not is_cloud[i][j]:
                cloud.append([i, j])
                basket[i][j] -= 2
    get_is_cloud()

N, M = map(int, input().split())
basket = [list(map(int, input().split())) for _ in range(N)]

is_cloud = [[False] * N for _ in range(N)]
cloud = []

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, -1, 1]

is_cloud[N - 2][0] = True
is_cloud[N - 2][1] = True
is_cloud[N - 1][0] = True
is_cloud[N - 1][1] = True

get_cloud()

for _ in range(M):
    d, s = map(int, input().split())
    move_rain(d, s)
    water_copy()
    make_cloud()

water_sum = 0
for i in range(N):
    for j in range(N):
        water_sum += basket[i][j]

print(water_sum)