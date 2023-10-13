def check(cur, num):
    global cnt
    if cur == len(arr):
        if num == s:
            print(cur, num, s)
            cnt += 1
            return
        return
    check(cur + 1, num + arr[cur])
    check(cur + 1, num)
    

n, s = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
check(0, 0)

if s == 0:
    cnt - 1
print(cnt)