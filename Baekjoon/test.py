import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]

pref_num = [[[0] * 11 for _ in range(n + 1)] for _ in range(n + 1)]

for x in range(1, n + 1):
    for y in range(1, n + 1):
        for k in range(11):
            if arr[x - 1][y - 1] == k:
                pref_num[x][y][k] += 1
            pref_num[x][y][k] += pref_num[x - 1][y][k] + pref_num[x][y - 1][k] - pref_num[x - 1][y - 1][k]

q = int(input().strip())
for _ in range(q):
    ax, ay, bx, by = map(int, input().split())
    ans = 0
    for i in range(1, 11):
        if pref_num[bx][by][i] - pref_num[bx][ay - 1][i] - pref_num[ax - 1][by][i] + pref_num[ax - 1][ay - 1][i]:
            ans += 1
    print(ans)


    
# for i in range(n + 1):


# n, k = map(int, input().split())

# if n == k:
#     print('Impossible')
# elif n == k + 1:
#     for i in range(1, n + 1):
#         print(i, end=' ')
# else:
#     arr = [i for i in range(1, n + 1)]
#     cnt = n - 1
#     turn = 1
#     while True:
#         if cnt == k:
#             break
#         if turn >= n - 1:
#             break
#         if cnt % 2 == 1:
#             arr[0], arr[n - 1] = arr[n - 1], arr[0]
#             cnt -= 1
#         elif cnt % 2 == 0:
#             arr[turn], arr[turn + 1] = arr[turn + 1], arr[turn]
#             cnt -= 2
#             turn += 2

#     print(*arr)
