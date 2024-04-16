import sys
input = sys.stdin.readline

def move(d, arr):
    maxx = 0
    for _ in range(d):
        arr = next(arr)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        cur = 0
        tmp = []
        for j in range(n):
            if cur == 0:
                cur = arr[i][j]
            elif cur != 0 and arr[i][j] != 0:
                if cur == arr[i][j]:
                    tmp.append(cur * 2)
                    cur = 0
                else:
                    tmp.append(cur)
                    cur = arr[i][j]
        tmp.append(cur)
        for idx in range(n):
            if idx < len(tmp):
                res[i][idx] = tmp[idx]
            else:
                res[i][idx] = 0
        maxx = max(maxx, max(res[i]))
    for i in range(4 - d):
        res = next(res)
    return res, maxx
    
                
def next(arr):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[j][n - i - 1] = arr[i][j]
    return res


def bfs(cur, arr):
    global ans
    if cur == 5:
        return
    for i in range(4):
        res, maxx = move(i, arr)
        ans = max(ans, maxx)
        bfs(cur + 1, res)

n = int(input().strip())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
bfs(0, board)
print(ans)