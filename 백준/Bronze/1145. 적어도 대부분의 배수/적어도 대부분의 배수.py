import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

ans = min(arr)
while True:
    cnt = 0
    for i in arr:
        if ans % i == 0:
            cnt += 1
    if cnt > 2:
        print(ans)
        break
    ans += 1