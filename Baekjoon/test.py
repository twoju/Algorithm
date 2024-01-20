import sys
input = sys.stdin.readline

n = int (input().strip())
# n 까지 소수 구하기
# 소수 범위 안에서 s, e 로 범위 좁히면서 찾기

prime = []
flag = [False, False] + [True] * (n - 1)

for i in range(2, n + 1):
    if flag[i]:
        prime.append(i)
        for j in range(i * 2, n + 1, i):
            flag[j] = False

s, e = 0, 0
cnt = 0
while e < len(prime):
    p = sum(prime[s:e+1])
    if p == n:
        cnt += 1
    if p >= n:
        s += 1
    else:
        e += 1
    
print(cnt)

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
