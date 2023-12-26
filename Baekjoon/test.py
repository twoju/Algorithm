import sys
input = sys.stdin.readline

n, k = map(int, input().split())

if n == k:
    print('Impossible')
elif n == k + 1:
    for i in range(1, n + 1):
        print(i, end=' ')
else:
    arr = [i for i in range(1, n + 1)]
    cnt = n - 1
    turn = 1
    while True:
        if cnt == k:
            break
        if turn >= n - 1:
            break
        if cnt % 2 == 1:
            arr[0], arr[n - 1] = arr[n - 1], arr[0]
            cnt -= 1
        elif cnt % 2 == 0:
            arr[turn], arr[turn + 1] = arr[turn + 1], arr[turn]
            cnt -= 2
            turn += 2

    print(*arr)
