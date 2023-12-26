a, b, n, w = map(int, input().split())

if n == 2:
    if a + b == w:
        print(1, 1)
    else:
        print(-1)
else:
    cnt = 0
    ans = []
    for x in range(1, n):
        if (a * x) + (b * (n - x)) == w:
            cnt += 1
            ans.append([x, n - x])
        if cnt > 1:
            break

    if len(ans) == 1:
        print(*ans[0])
    else:
        print(-1)