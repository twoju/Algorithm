N, K = map(int, input().split())
arr = [i for i in map(int, input().split())]
check = [0] * (max(arr) + 1)

ans = 0
s, e = 0, 0

while e < N:
    if s > e:
        break
    if check[arr[e]] < K:
        check[arr[e]] += 1
        e += 1
    else:
        check[arr[s]] -= 1
        s += 1
    ans = max(ans, e - s)
print(ans)
