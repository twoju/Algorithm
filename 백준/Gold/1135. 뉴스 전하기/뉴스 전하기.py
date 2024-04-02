import sys
input = sys.stdin.readline

def check(cur):
    tmp = []
    for nxt in graph[cur]:
        check(nxt)
        tmp.append(dp[nxt])
    if tmp:
        tmp.sort(reverse=True)
        cnt = 0
        for i in range(len(tmp)):
            if tmp[i] + i + 1 > cnt:
                cnt = tmp[i] + i + 1
        dp[cur] = cnt

n = int(input().strip())
graph = [[] for _ in range(n)]
arr = list(map(int, input().split()))

for i in range(1, n):
    graph[arr[i]].append(i)

dp = [0] * n
check(0)
print(max(dp))