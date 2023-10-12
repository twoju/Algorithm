def recur(cur, s, b):
    global ans
    if cur == n:
        if s == 1 and b == 0:
            return
        ans = min(ans, abs(s - b))
        return
    recur(cur + 1, s * taste[cur][0], b + taste[cur][1])
    recur(cur + 1, s, b)
    

n = int(input())
taste = [list(map(int, input().split())) for _ in range(n)]

ans = abs(taste[0][0] - taste[0][1])
recur(0, 1, 0)
print(ans)