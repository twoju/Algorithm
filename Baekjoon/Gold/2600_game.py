def recur(f, s):
    if dp[f][s] != -1:
        return dp[f][s]
    
    for i in range(3):
        if able[i] <= f and not recur(f - able[i], s):
            dp[f][s] = 1
            return dp[f][s]
    for i in range(3):
        if able[i] <= s and not recur(f, s - able[i]):
            dp[f][s] = 1
            return dp[f][s]
    dp[f][s] = 0
    return dp[f][s]


able = list(map(int, input().split()))
dp = [[-1] * 501 for _ in range(501)]
for _ in range(5):
    first, second = map(int, input().split())
    if recur(first, second):
        print("A")
    else:
        print("B")