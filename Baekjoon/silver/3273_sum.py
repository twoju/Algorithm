N = int(input())
arr = sorted([i for i in map(int, input().split())])
X = int(input())

ans = 0
s, e = 0, N - 1
while True:
    if s >= e:
        break
    if arr[s] + arr[e] == X:
        ans += 1
        s += 1
        e -= 1
    elif arr[s] + arr[e] > X:
        e -= 1
    else:
        s += 1

print(ans)