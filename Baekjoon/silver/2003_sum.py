N, M = map(int, input().split())

arr = [i for i in map(int, input().split())]

ans = 0
i, j = 0, 0
while j < N and i <= j:
    total = sum(arr[i:j+1])
    if total == M:
        ans += 1
        i += 1
    elif total < M:
        if j == N:
            break
        j += 1
    else:
        i += 1

print(ans)