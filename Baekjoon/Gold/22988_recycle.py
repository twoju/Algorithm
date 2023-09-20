N, X = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(arr)
cnt = 0

s, e = 0, len(arr) - 1

for i in range(e, -1, -1):
    if arr[i] == X:
        cnt += 1
        e = i - 1
etc = len(arr) - cnt
while True:
    if s >= e:
        break
    if arr[s] + arr[e] >= X/2:
        cnt += 1
        s += 1
        e -= 1
        etc -= 2
    else:
        s += 1

print(cnt + etc // 3)