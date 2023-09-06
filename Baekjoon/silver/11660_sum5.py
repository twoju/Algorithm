import sys
sys.stdin = open('11660_sum.txt', 'r')

N, M = map(int, sys.stdin.readline().split())

prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]

input = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + input[i - 1][j - 1]

for _ in range(M):
    ans = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    ans += prefix_sum[x2][y2] - prefix_sum[x2][y1 - 1] - prefix_sum[x1 - 1][y2] + prefix_sum[x1 - 1][y1 - 1]
    print(ans)