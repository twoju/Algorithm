import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)

def recur(cur, prev):
    for nxt in graph[cur]:
        if nxt == prev:
            continue
        if dp[nxt][0] or dp[nxt][1]:
            continue
        recur(nxt, cur)
        dp[cur][1] += dp[nxt][0]
        dp[cur][0] += max(dp[nxt][0], dp[nxt][1] + citizen[nxt])

n = int(input().strip())
citizen = [0] + list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 인접하지 않은 마을들 사이의 인구 합이 최대로
# 우수마을이 아닌 곳은 하나의 마을은 꼭 연결 되어야함
    
dp = [[0] * 2 for _ in range(n + 1)]
dp[1][1] = citizen[1]

recur(1, 1)
print(max(dp[1]))