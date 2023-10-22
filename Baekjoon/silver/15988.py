# def recur(total):
#     global ans
#     if total > n:
#         return
#     if total == n:
#         ans += 1
#         return
#     for i in range(1, 4):
#         recur(total + i)


# 재귀로 풀었더니 recursion error 랑 시간초과를 뿜어낸다..
# pypy 는 메모리 초과
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def recur(total):
    if total > n:
        return 0
    if total == n:
        return 1
    if dp[total] != -1:
        return dp[total]
    ans = 0
    for i in range(1, 4):
        ans += recur(total + i)
        dp[total] = ans
    return dp[total] % 1000000009


t = int(input())

for _ in range(t):
    n = int(input())
    dp = [-1] * 1000001
    print(recur(0))

# ---

import sys
input = sys.stdin.readline

t = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 1000001):
    dp[i] = dp[i - 1] % 1000000009 + dp[i - 2] % 1000000009 + dp[i - 3] % 1000000009
for _ in range(t):
    n = int(input())
    print(dp[n] % 1000000009)


# 푸는 방법
# dp에서 1, 2, 3을 더할 수 있으니까 그만큼 이전의 dp 값을 가져오고 1을 더해서
# dp에 넣어주는 방식으로 쭉쭉 올라가다가
# max(dp)를 출력하면 되나?

