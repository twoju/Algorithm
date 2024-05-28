import sys
input = sys.stdin.readline

def recur(cur, cnt):
    if cnt > w:
        return -123123123
    if cur == t:
        return 0
    if dp[cur][cnt] != -1:
        return dp[cur][cnt]
    ret = -123123123
    if (cnt % 2 and tree[cur] == 2) or (cnt % 2 == 0 and tree[cur] == 1):
        ret = max(recur(cur + 1, cnt + 1) + 1, recur(cur + 1, cnt) + 1)
    else:
        ret = max(recur(cur + 1, cnt), recur(cur + 1, cnt + 1))
    dp[cur][cnt] = ret
    return dp[cur][cnt]
    

t, w = map(int, input().split())
tree = [int(input().strip()) for _ in range(t)]
dp = [[-1] * 31 for _ in range(1010)]
print(max(recur(0, 0), recur(0, 1)))