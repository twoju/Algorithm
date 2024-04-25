import sys
input = sys.stdin.readline
from collections import deque

a, b, c, n = map(int, input().split())

if a == 1:
    print(1)
    sys.exit(0)
    
q = deque()
q.append(0)
while q:
    cur = q.popleft()
    if cur > n:
        print(0)
        break
    if cur == n:
        print(1)
        break
    for nxt in [c, b, a]:
        q.append(cur + nxt)

