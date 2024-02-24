import sys
input = sys.stdin.readline

def recur(a, b):
    if dp[a][b] != -1:
        return dp[a][b]
    
    cnt = 0
    for i in arr:
        if i <= a and not recur(a - i, b):
            cnt += 1
        if i <= b and not recur(a, b - i):
            cnt += 1
        if cnt == 0:
            dp[a][b] = False
        else:
            dp[a][b] = True
    return dp[a][b]

arr = list(map(int, input().split()))

for _ in range(5):
    x, y = map(int, input().split())
    dp = [[-1] * 550 for _ in range(550)]
    if recur(x, y):
        print('A')
    else:
        print('B')