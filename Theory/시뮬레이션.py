"""
1. 설계
2. 데이터 저장을 어떻게 할지?

# 먀법사 문제
1. 문제를 작게 잘라서 함수를 설계해준다

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

for _ in range(m):
    d, s = map(int, input().split())
    move(d, s)
    rain()
    gone()
    watercopy()
    makecloud()
"""

def get_exist(): # cloud 배열 기준으로 exist 배열 채우기
    global exist
    # 먼저 배열 초기화
    exist = [[False] * n for _ in range(n)]
    for x, y in cloud:
        exist[x][y] = True
    

def get_cloud(): # exist 기반으로 cloud 채우기
    global cloud
    # 먼저 배열 초기화
    cloud = []
    for i in range(n):
        for j in range(n):
            if exist[i][j]:
                cloud.append([i, j])

def move(d, s):
    for i in range(len(cloud)):
        x = cloud[i][0]
        y = cloud[i][1]
        for j in range(s):
            x = (x + dxy[d][0] + n) % n
            y = (y + dxy[d][1] + n) % n
        cloud[i][0] = x
        cloud[i][1] = y
    # cloud 가 값 변경을 했으니까 exist 도 변경
    get_exist()

def rain():
    for i in range(n):
        for j in range(n):
            if exist[i][j]:
                board[i][j] += 1

"""
배열 밖으로 넘어가는 경우는 모듈러 연산으로 해결 가능
            x = (x + dxy[d][0] + n) % n
            y = (y + dxy[d][1] + n) % n
"""

def watercopy():
    # 동시에 진행하지만 원본이 변경되면 안될 때 배열 복사
    copy_basket = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            copy_basket[i][j] = board[i][j]
    # copy_basket = [i[:] for i in board]
    for i in range(n):
        for j in range(n):
            if not exist[i][j]:
                continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if copy_basket[nx][ny] != 0:
                    board[i][j] += 1

def makecloud():
    global cloud
    cloud = []
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and not exist[i][j]:
                cloud.append([i, j])
                board[i][j] -= 2
    get_cloud()


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 구름의 위치를 저장해야함
# 구름의 위치 나타내는 방법
# 1. (x, y) 로 저장하기
# 2. 2차원 배열을 만들어서 Boolean 으로 표시하기
# 고민하지 않고 두 배열 모두 사용하면 된다.

# 구름이 있는 곳 체크
exist = [[False] * n for _ in range(n)]
# 쳐음에 구름이 있는 위치 표시해주기
cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
# cloud를 채웠으니까 아래 함수 호출하면 exist 도 설정 된다.
get_exist()

dxy = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1),]

dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]


for _ in range(m):
    d, s = map(int, input().split())
    move(d, s)
    rain()
    watercopy()
    makecloud()

ans = 0
for i in range(n):
    for j in range(n):
        ans += board[i][j]
print(ans)

"""
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
4방향 확인할 때, 정해진게 없으면 교차되는 숫자로 하면 좋다
"""