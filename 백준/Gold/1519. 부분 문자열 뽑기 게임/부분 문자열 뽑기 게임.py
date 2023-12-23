import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())

def recur(cur):
    if cur < 10:
        return False
    
    if dp[cur] != -1:
        return dp[cur]
    
    cnt = 0
    str_cur = str(cur)
    for i in range(1, len(str_cur) + 1):
        for j in range(i):
            now_str = cur % 10 ** i // 10 ** j
            if now_str >= cur or 0 >= now_str: continue

            nxt = cur - now_str
            if not recur(nxt):
                cnt = 1
                break
        if cnt:
            break
    dp[cur] = cnt
    return dp[cur]

dp = [-1] * (n + 1)


if recur(n):
    for i in range(10):
        dp[i] = 0
    ans = 1e9
    str_n = str(n)
    for i in range(1, len(str_n) + 1):
        for j in range(i):
            now_str = n % 10 ** i // 10 ** j
            if now_str >= n or 0 >= now_str: continue

            nxt = n - now_str
            if recur(nxt) == 0:
                ans = min(ans, now_str)
    print(ans)
else:
    print(-1)