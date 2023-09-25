def check(l, r, dist):
    while l <= r:
        mid = (l + r) // 2
        if dots[mid] == dist:
            return 1
        if dots[mid] > dist:
            r = mid - 1
        else:
            l = mid + 1
    return 0

T = int(input())
for _ in range(T):
    cnt = 0
    N = int(input())
    dots = sorted(list(map(int, input().split())))

    l, r = 0, N - 1

    for i in range(N - 1):
        for j in range(i + 1, N):
            dist = abs(dots[j] - dots[i])
            if check(l, r, dots[j] + dist):
                cnt += 1

    print(cnt)