import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
time = [0 for _ in range(n + 1)]
ans = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
able = [0 for _ in range(n + 1)]
start = []

for i in range(1, n + 1):
    arr = list(map(int, input().split()))
    if len(arr) == 2:
        start.append(i)
    time[i] += arr[0]
    for j in arr[1:-1]:
        graph[j].append(i)
        able[i] -= 1

q = deque()
for i in start:
    q.append(i)
    ans[i] += time[i]

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        able[nxt] += 1
        ans[nxt] = max(ans[nxt], ans[cur] + time[nxt])
        if not able[nxt]: q.append(nxt)

for i in range(1, n + 1):
    print(ans[i])