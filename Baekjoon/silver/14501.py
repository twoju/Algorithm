def work(cur, pay):
    global res
    if cur == n:
        res = max(res, pay)
        return
    if cur > n:
        return
    work(cur + arr[cur][0], pay + arr[cur][1])
    work(cur + 1, pay)
    

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

res = 0
work(0, 0)
print(res)