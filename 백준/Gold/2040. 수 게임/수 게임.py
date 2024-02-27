import sys
input = sys.stdin.readline
sys.setrecursionlimit(4000)

def recur(cur):
    if cur > n:
        return 0
    if dp[cur] != -100000:
        return dp[cur]
    ret = 1e9
    for i in range(cur, n + 1):
        ret = min(ret, pref_sum[i] - pref_sum[cur - 1] - recur(i + 1))
    dp[cur] = ret
    return dp[cur]


n = int(input())
for _ in range(3):
    arr = list(map(int, input().split()))
    arr.reverse()
    pref_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        pref_sum[i] = pref_sum[i - 1] + arr[i - 1]

    dp = [-100000] * 3030
    ans = recur(1)

    if ans < 0:
        print('A')
    elif ans > 0:
        print('B')
    else:
        print('D')