N = int(input())

ans = 1
if N < 4: print(ans)
else:
    for i in range(2, int(N ** 0.5) + 1):
        if i ** 2 <= N:
            ans += 1
    print(ans)