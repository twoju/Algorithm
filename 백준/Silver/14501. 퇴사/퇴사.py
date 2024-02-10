import sys
input = sys.stdin.readline

def recur(cur, pay):
    global ans
    if cur == n:
        ans = max(ans, pay)
        return
    if cur > n:
        return
    recur(cur + arr[cur][0], pay + arr[cur][1])
    recur(cur + 1, pay)
    

n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
recur(0, 0)
print(ans)