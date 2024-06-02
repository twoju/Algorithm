import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    arr = list(map(int, input().split()))
    n = arr[0]
    avg = sum(arr[1:]) / n
    cnt = 0
    for i in range(1, n + 1):
        if arr[i] > avg:
            cnt += 1
    print(round(cnt / n * 100, 3), '%')